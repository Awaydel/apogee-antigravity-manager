import os
import re
import ssl
import json
import time
import urllib.request
import subprocess
from datetime import datetime, timezone

class LanguageServerClient:
    def __init__(self, user_agent='Antigravity/2.12.2'):
        self.user_agent = user_agent
        self.cache = {'pid': None, 'port': None, 'csrf': None, 'last_checked': 0}
        self.ssl_ctx = ssl.create_default_context()
        self.ssl_ctx.check_hostname = False
        self.ssl_ctx.verify_mode = ssl.CERT_NONE

    def get_connection(self, force_refresh=False):
        now = time.time()
        if not force_refresh and (now - self.cache['last_checked'] < 5) and self.cache.get('port') and self.cache.get('csrf'):
            return self.cache

        try:
            ps_cmd = "(Get-CimInstance Win32_Process -Filter \"name = 'language_server.exe'\") | ForEach-Object { [string]::Concat($_.ProcessId, '|', $_.CommandLine) }"
            out = subprocess.check_output(['powershell', '-NoProfile', '-Command', ps_cmd], timeout=4).decode('utf-8', errors='ignore')
        except Exception:
            self.cache.update({'pid': None, 'port': None, 'csrf': None, 'last_checked': now})
            return self.cache

        pid, csrf, port = None, None, None
        for line in out.splitlines():
            if 'language_server' in line:
                parts = line.split('|', 1)
                if len(parts) >= 2 and parts[0].strip().isdigit():
                    pid = int(parts[0].strip())
                cmd = parts[1] if len(parts) >= 2 else line
                m_csrf = re.search(r'--csrf_token\s+([0-9a-fA-F\-]+)', cmd)
                m_port = re.search(r'--https_server_port\s+(\d+)', cmd)
                if m_csrf:
                    csrf = m_csrf.group(1).strip()
                if m_port:
                    parsed_port = int(m_port.group(1).strip())
                    if parsed_port > 0:
                        port = parsed_port
                if csrf and port:
                    break

        if (not port or port == 0) and pid:
            try:
                net_out = subprocess.check_output(f'netstat -ano | findstr {pid}', shell=True, timeout=3).decode('utf-8', errors='ignore')
                for l in net_out.splitlines():
                    if 'LISTENING' in l:
                        parts = l.split()
                        if len(parts) >= 2 and ':' in parts[1]:
                            cand = int(parts[1].split(':')[-1])
                            try:
                                req = urllib.request.Request(f'https://127.0.0.1:{cand}/', headers={'User-Agent': self.user_agent})
                                with urllib.request.urlopen(req, context=self.ssl_ctx, timeout=0.4) as resp:
                                    if resp.status == 200:
                                        port = cand
                                        break
                            except Exception:
                                pass
            except Exception:
                pass

        self.cache.update({'pid': pid, 'port': port, 'csrf': csrf, 'last_checked': now})
        return self.cache

    def rpc(self, method, payload=None):
        payload = payload or {}
        conn = self.get_connection()
        port, csrf = conn.get('port'), conn.get('csrf')
        if not port or not csrf:
            conn = self.get_connection(force_refresh=True)
            port, csrf = conn.get('port'), conn.get('csrf')
            if not port or not csrf:
                return None

        url = f"https://127.0.0.1:{port}/exa.language_server_pb.LanguageServerService/{method}"
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'Connect-Protocol-Version': '1',
                'X-Codeium-Csrf-Token': csrf,
                'User-Agent': self.user_agent
            }
        )
        try:
            with urllib.request.urlopen(req, context=self.ssl_ctx, timeout=3) as resp:
                if resp.status == 200:
                    raw = resp.read()
                    return json.loads(raw.decode('utf-8')) if raw else {}
        except Exception:
            conn = self.get_connection(force_refresh=True)
            port, csrf = conn.get('port'), conn.get('csrf')
            if not port or not csrf:
                return None
            url = f"https://127.0.0.1:{port}/exa.language_server_pb.LanguageServerService/{method}"
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode('utf-8'),
                headers={
                    'Content-Type': 'application/json',
                    'Connect-Protocol-Version': '1',
                    'X-Codeium-Csrf-Token': csrf,
                    'User-Agent': self.user_agent
                }
            )
            try:
                with urllib.request.urlopen(req, context=self.ssl_ctx, timeout=3) as resp:
                    if resp.status == 200:
                        raw = resp.read()
                        return json.loads(raw.decode('utf-8')) if raw else {}
            except Exception:
                pass
        return None

    def grpc_web(self, service_method, body=b'{}'):
        conn = self.get_connection()
        port, csrf = conn.get('port'), conn.get('csrf')
        if not port or not csrf:
            conn = self.get_connection(force_refresh=True)
            port, csrf = conn.get('port'), conn.get('csrf')
            if not port or not csrf:
                return None

        url = f"https://127.0.0.1:{port}/exa.language_server_pb.LanguageServerService/{service_method}"
        # 1 byte compression flag (0x00) + 4 bytes big-endian length prefix
        frame = bytearray([0])
        frame.extend(len(body).to_bytes(4, 'big'))
        frame.extend(body)

        req = urllib.request.Request(
            url,
            data=bytes(frame),
            headers={
                'Content-Type': 'application/grpc-web+json',
                'x-codeium-csrf-token': csrf,
                'x-grpc-web': '1',
                'x-user-agent': 'CONNECT_ES_USER_AGENT'
            }
        )
        try:
            with urllib.request.urlopen(req, context=self.ssl_ctx, timeout=3) as resp:
                raw = resp.read()
                if len(raw) >= 5:
                    msg_len = int.from_bytes(raw[1:5], 'big')
                    return json.loads(raw[5:5+msg_len].decode('utf-8'))
        except Exception:
            pass
        return None

    def get_user_status(self):
        return self.rpc("GetUserStatus")

    def get_quota_summary(self):
        raw = self.grpc_web('RetrieveUserQuotaSummary', b'{}')
        if not raw or 'response' not in raw:
            return None

        groups = raw.get('response', {}).get('groups', [])
        now_utc = datetime.now(timezone.utc)

        def parse_bucket(b):
            if not b:
                return None
            frac = b.get('remainingFraction')
            pct = round(frac * 100, 1) if frac is not None else 100.0
            reset_time = b.get('resetTime', '')
            local_reset = ''
            rem_secs = 0
            desc = b.get('description', '')
            if reset_time:
                try:
                    dt = datetime.strptime(reset_time[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc)
                    rem_secs = max(0, int((dt - now_utc).total_seconds()))
                    days = int(rem_secs // 86400)
                    hours = int((rem_secs % 86400) // 3600)
                    mins = int((rem_secs % 3600) // 60)
                    if days > 0:
                        local_reset = dt.astimezone().strftime('%d.%m %H:%M')
                        if not desc: desc = f"Reset in {days}d {hours}h"
                    elif hours > 0:
                        local_reset = dt.astimezone().strftime('%H:%M')
                        if not desc: desc = f"Reset in {hours}h {mins}m"
                    else:
                        local_reset = dt.astimezone().strftime('%H:%M')
                        if not desc: desc = f"Reset in {mins}m"
                except Exception:
                    local_reset = reset_time

            return {
                'bucketId': b.get('bucketId', ''),
                'displayName': b.get('displayName', ''),
                'window': b.get('window', ''),
                'remainingFraction': frac if frac is not None else 1.0,
                'percentage': pct,
                'resetTime': reset_time,
                'resetTimeLocal': local_reset,
                'resetSeconds': rem_secs,
                'description': desc
            }

        gemini_data = {'weekly': None, 'session5h': None}
        claude_gpt_data = {'weekly': None, 'session5h': None}

        for g in groups:
            dname = g.get('displayName', '').lower()
            buckets = g.get('buckets', [])
            w_bucket = next((b for b in buckets if b.get('window') == 'weekly'), None)
            h_bucket = next((b for b in buckets if b.get('window') in ('5h', 'hourly')), None)

            if 'gemini' in dname:
                gemini_data['weekly'] = parse_bucket(w_bucket)
                gemini_data['session5h'] = parse_bucket(h_bucket)
            elif 'claude' in dname or 'gpt' in dname:
                claude_gpt_data['weekly'] = parse_bucket(w_bucket)
                claude_gpt_data['session5h'] = parse_bucket(h_bucket)

        return {
            'gemini': gemini_data,
            'claudeGpt': claude_gpt_data,
            'systemDescription': raw.get('response', {}).get('description', '')
        }

    def get_state_file_path(self):
        candidates = [
            os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'home', '.gemini', 'antigravity', 'antigravity_state.pbtxt'),
            os.path.expandvars(r'%USERPROFILE%\.gemini\antigravity\antigravity_state.pbtxt')
        ]
        for p in candidates:
            p = os.path.abspath(p)
            if os.path.exists(p):
                return p
        return None

    def set_active_model(self, mid):
        p = self.get_state_file_path()
        if not p:
            return False
        try:
            with open(p, 'r', encoding='utf-8') as f:
                text = f.read()
            if re.search(r'last_selected_agent_model:\s*[A-Za-z0-9_]+', text):
                new_text = re.sub(r'last_selected_agent_model:\s*[A-Za-z0-9_]+', f'last_selected_agent_model: {mid}', text)
            else:
                new_text = text.rstrip() + f'\nlast_selected_agent_model: {mid}\n'
            with open(p, 'w', encoding='utf-8') as f:
                f.write(new_text)
            return True
        except Exception:
            return False

    def get_active_model(self, model_map=None):
        model_map = model_map or {}

        def resolve_name(raw_id):
            if not raw_id:
                return 'Gemini 3.8 Flash (Medium)'
            if raw_id in model_map:
                return model_map[raw_id]
            low = raw_id.lower()
            if 'm35' in low or 'sonnet' in low: return 'Claude Sonnet 4.6 (Thinking)'
            elif 'm26' in low or 'opus' in low: return 'Claude Opus 4.6 (Thinking)'
            elif 'gpt' in low or 'oss' in low: return 'GPT-OSS 120B (Medium)'
            elif 'm16' in low: return 'Gemini 3.1 Pro (High)'
            elif 'm36' in low: return 'Gemini 3.1 Pro (Low)'
            elif 'm319' in low: return 'Gemini 3.8 Flash (Medium)'
            elif 'm318' in low: return 'Gemini 3.8 Flash (High)'
            elif 'm322' in low: return 'Claude Sonnet 4.6'
            elif 'm323' in low: return 'Claude Opus 4.6'
            return raw_id

        # 1. Primary: query live cascade trajectory from Language Server RPC
        try:
            all_t = self.rpc("GetAllCascadeTrajectories")
            if all_t and "trajectorySummaries" in all_t:
                summaries = all_t["trajectorySummaries"]
                if summaries:
                    sorted_s = sorted(
                        summaries.items(),
                        key=lambda x: x[1].get('lastModifiedTime', '') or x[1].get('lastUserInputTime', '') or x[1].get('createdTime', ''),
                        reverse=True
                    )
                    latest_cid = sorted_s[0][0]
                    traj = self.rpc("GetCascadeTrajectory", {"cascadeId": latest_cid})
                    if traj and "trajectory" in traj:
                        gm_list = traj["trajectory"].get("generatorMetadata", [])
                        if gm_list:
                            for gm in reversed(gm_list):
                                mid = (
                                    gm.get("customMetadata", {}).get("model_enum") or
                                    gm.get("chatModel", {}).get("model") or
                                    gm.get("responseModel")
                                )
                                if mid:
                                    return {'rawId': mid, 'name': resolve_name(mid)}
        except Exception:
            pass

        # 2. Secondary fallback: check antigravity_state.pbtxt
        p = self.get_state_file_path()
        if p:
            try:
                with open(p, 'r', encoding='utf-8') as f:
                    content = f.read()
                m = re.search(r'last_selected_agent_model:\s*([A-Za-z0-9_]+)', content)
                if m:
                    raw_id = m.group(1).strip()
                    return {'rawId': raw_id, 'name': resolve_name(raw_id)}
            except Exception:
                pass

        return {'rawId': 'MODEL_PLACEHOLDER_M319', 'name': 'Gemini 3.8 Flash (Medium)'}

