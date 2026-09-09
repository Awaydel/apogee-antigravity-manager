#!/usr/bin/env python3
import os
import sys
import json
import time
import argparse
import webbrowser
import subprocess
import urllib.parse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from datetime import datetime, timezone

from core.client import LanguageServerClient
from core.accounts import AccountManager
from core.telemetry import TelemetryTracker

WEB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web')

client = LanguageServerClient()
accounts = AccountManager()
telemetry = TelemetryTracker(client)

def is_ide_running():
    try:
        out = subprocess.check_output('tasklist /FI "IMAGENAME eq Antigravity.exe" /NH', shell=True).decode('utf-8', errors='ignore')
        return 'Antigravity.exe' in out
    except Exception:
        return False

def stop_ide():
    try:
        subprocess.run('taskkill /F /IM Antigravity.exe /T', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1.5)
        return True
    except Exception:
        return False

def start_ide():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(base_dir, '..', 'AntigravityPortable.bat'),
        os.path.join(base_dir, '..', 'App', 'Antigravity', 'Antigravity.exe'),
        os.path.join(base_dir, '..', 'Antigravity.exe'),
        os.path.expandvars(r'%LOCALAPPDATA%\Programs\Antigravity\Antigravity.exe'),
        os.path.expandvars(r'%PROGRAMFILES%\Antigravity\Antigravity.exe'),
        os.path.expandvars(r'%USERPROFILE%\AppData\Local\Programs\Antigravity\Antigravity.exe')
    ]
    for exe in candidates:
        if os.path.exists(exe):
            try:
                subprocess.Popen([exe], cwd=os.path.dirname(exe), shell=True)
                return True
            except Exception:
                pass
    return False

def get_live_status():
    status_resp = client.get_user_status()
    quota_summary = client.get_quota_summary()

    buckets = []
    model_map = {}
    tier_name = 'Google AI Pro'
    user_avatar = ''

    if status_resp and 'userStatus' in status_resp:
        us = status_resp['userStatus']
        tier_name = us.get('userTier', {}).get('name') or 'Google AI Pro'
        user_avatar = us.get('profilePictureUrl') or ''
        configs = us.get('cascadeModelConfigData', {}).get('clientModelConfigs', [])
        now_utc = datetime.now(timezone.utc)

        for c in configs:
            label = c.get('label', '')
            raw_mid = c.get('modelOrAlias', {}).get('model', '')
            if raw_mid:
                model_map[raw_mid] = label

            q = c.get('quotaInfo', {})
            frac = q.get('remainingFraction')
            pct = round(frac * 100, 1) if frac is not None else 100.0
            reset_time = q.get('resetTime', '')
            local_reset = ''
            if reset_time:
                try:
                    dt = datetime.strptime(reset_time[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc)
                    local_reset = dt.astimezone().strftime('%H:%M')
                except Exception:
                    local_reset = reset_time

            low = label.lower()
            if 'claude' in low:
                brand, provider, icon, group_key = 'claude', 'Anthropic', 'assets/claude.svg', 'claudeGpt'
            elif 'gpt' in low:
                brand, provider, icon, group_key = 'openai', 'OpenAI', 'assets/openai.svg', 'claudeGpt'
            else:
                brand, provider, icon, group_key = 'gemini', 'Google', 'assets/gemini.svg', 'gemini'

            buckets.append({
                'modelId': raw_mid,
                'name': label,
                'provider': provider,
                'brand': brand,
                'icon': icon,
                'groupKey': group_key,
                'percentage': pct,
                'remainingFraction': frac,
                'resetTime': reset_time,
                'resetTimeLocal': local_reset,
                'isPremium': 'claude' in low or 'gpt' in low,
                'isThinking': 'thinking' in low,
                'isRecommended': c.get('isRecommended', False)
            })

        buckets.sort(key=lambda x: (0 if x['brand'] == 'claude' else (1 if x['brand'] == 'openai' else 2), x['name']))

    active_model = client.get_active_model(model_map)
    conn = client.get_connection()

    return {
        'tier': tier_name,
        'userAvatar': user_avatar,
        'quotaSummary': quota_summary,
        'buckets': buckets,
        'activeModel': active_model,
        'modelMap': model_map,
        'lsPid': conn.get('pid'),
        'lsPort': conn.get('port')
    }

class ApogeeHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError):
            pass

    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        if path == '/api/status':
            db = accounts.load_db()
            active_email = db.get('active_email')
            live = get_live_status()

            if live.get('userAvatar') and active_email:
                for acc in db.get('accounts', []):
                    if acc.get('email') == active_email and not acc.get('picture'):
                        acc['picture'] = live['userAvatar']
                        accounts.save_db(db)
                        break

            self.send_json({
                'activeEmail': active_email,
                'isIdeRunning': is_ide_running(),
                'accounts': db.get('accounts', []),
                'activeModel': live.get('activeModel'),
                'liveQuotas': live.get('buckets', []),
                'quotaSummary': live.get('quotaSummary'),
                'tier': live.get('tier', 'Google AI Pro'),
                'lsPid': live.get('lsPid'),
                'lsPort': live.get('lsPort')
            })
        elif path in ('/api/tokens', '/api/token-usage'):
            live = get_live_status()
            report = telemetry.get_token_report(live.get('modelMap'))
            self.send_json(report)
        elif path == '/api/restart_ls':
            try:
                subprocess.run('taskkill /F /IM language_server.exe', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(1.5)
                client.get_connection(force_refresh=True)
                self.send_json({'success': True})
            except Exception as e:
                self.send_json({'success': False, 'error': str(e)}, 500)
        elif path == '/api/restart_ide':
            stop_ide()
            time.sleep(1)
            start_ide()
            self.send_json({'success': True})
        elif path == '/api/export_accounts':
            db = accounts.load_db()
            payload = {
                'version': '5.0',
                'exported_at': datetime.now(timezone.utc).isoformat(),
                'accounts': db.get('accounts', []),
                'active_email': db.get('active_email')
            }
            body = json.dumps(payload, indent=2, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Disposition', 'attachment; filename="antigravity_accounts.json"')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif path == '/api/oauth/start':
            auth_url = (
                "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
                    'client_id': accounts.CLIENT_ID,
                    'redirect_uri': f'http://127.0.0.1:{self.server.server_port}/oauth/callback',
                    'response_type': 'code',
                    'scope': 'https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/cclog https://www.googleapis.com/auth/experimentsandconfigs',
                    'access_type': 'offline',
                    'prompt': 'consent'
                })
            )
            self.send_json({'auth_url': auth_url})
        elif path == '/oauth/callback':
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            code = query.get('code', [None])[0]
            if code:
                try:
                    data = urllib.parse.urlencode({
                        'code': code,
                        'client_id': accounts.CLIENT_ID,
                        'client_secret': accounts.CLIENT_SECRET,
                        'redirect_uri': f'http://127.0.0.1:{self.server.server_port}/oauth/callback',
                        'grant_type': 'authorization_code'
                    }).encode('utf-8')
                    req = urllib.request.Request('https://oauth2.googleapis.com/token', data=data)
                    with urllib.request.urlopen(req) as resp:
                        token_resp = json.loads(resp.read().decode('utf-8'))

                    uinfo = accounts.fetch_user_info(token_resp['access_token'])
                    email = uinfo.get('email')
                    if email:
                        db = accounts.load_db()
                        existing = next((a for a in db.get('accounts', []) if a.get('email') == email), None)
                        acc_entry = {
                            'email': email,
                            'name': uinfo.get('name', email.split('@')[0]),
                            'picture': uinfo.get('picture', ''),
                            'access_token': token_resp.get('access_token'),
                            'refresh_token': token_resp.get('refresh_token') or (existing.get('refresh_token') if existing else None),
                            'expires_at': int(time.time() + token_resp.get('expires_in', 3600)),
                            'tier': 'Pro'
                        }
                        if existing:
                            existing.update(acc_entry)
                        else:
                            db.setdefault('accounts', []).append(acc_entry)
                        db['active_email'] = email
                        accounts.save_db(db)

                        accounts.sync_files(email, acc_entry['access_token'], acc_entry['refresh_token'], acc_entry['expires_at'])
                        accounts.write_system_credential(token_resp)
                except Exception as e:
                    pass
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            super().do_GET()

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length > 0 else b'{}'
        try:
            payload = json.loads(body.decode('utf-8'))
        except Exception:
            payload = {}

        if path == '/api/switch':
            email = payload.get('email')
            db = accounts.load_db()
            target = next((a for a in db.get('accounts', []) if a.get('email') == email), None)
            if not target:
                self.send_json({'success': False, 'error': 'Account not found'}, 404)
                return

            if target.get('refresh_token'):
                try:
                    ref = accounts.refresh_token(target['refresh_token'])
                    if 'access_token' in ref:
                        target['access_token'] = ref['access_token']
                        target['expires_at'] = int(time.time() + ref.get('expires_in', 3600))
                        accounts.write_system_credential(ref)
                except Exception:
                    pass

            db['active_email'] = email
            accounts.save_db(db)
            accounts.sync_files(email, target.get('access_token'), target.get('refresh_token'), target.get('expires_at'))
            self.send_json({'success': True})
        elif path == '/api/select_model':
            mid = payload.get('modelId')
            mname = payload.get('name')
            if not mid:
                self.send_json({'success': False, 'error': 'Missing modelId'}, 400)
                return

            client.set_active_model(mid)
            db = accounts.load_db()
            db['active_model'] = {'rawId': mid, 'name': mname}
            accounts.save_db(db)
            self.send_json({'success': True, 'modelId': mid, 'name': mname})
        else:
            self.send_response(404)
            self.end_headers()

def main():
    parser = argparse.ArgumentParser(description='Apogee — Antigravity Language Server Dashboard')
    parser.add_argument('--port', type=int, default=28888, help='Server port (default: 28888)')
    parser.add_argument('--host', default='127.0.0.1', help='Host address (default: 127.0.0.1)')
    parser.add_argument('--no-browser', action='store_true', help='Do not open browser on startup')
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), ApogeeHandler)
    url = f'http://{args.host}:{args.port}/'
    print(f'Apogee server running at {url}')

    if not args.no_browser:
        webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down...')
        server.server_close()

if __name__ == '__main__':
    main()
