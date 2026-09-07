import os
import urllib.parse
from datetime import datetime, timezone

class TelemetryTracker:
    def __init__(self, client):
        self.client = client

    def get_token_report(self, model_map=None):
        model_map = model_map or {}
        all_t = self.client.rpc("GetAllCascadeTrajectories")
        if not all_t or "trajectorySummaries" not in all_t:
            return {
                'totalConversations': 0, 'totalTokens': 0, 'totalInputTokens': 0,
                'totalOutputTokens': 0, 'totalThinkingTokens': 0, 'totalCacheTokens': 0,
                'totalCalls': 0, 'conversations': [], 'modelsSummary': {}
            }

        summaries = all_t.get("trajectorySummaries", {})
        results = []
        overall_input = 0
        overall_output = 0
        overall_thinking = 0
        overall_cache = 0
        overall_calls = 0
        overall_models = {}

        now_utc = datetime.now(timezone.utc)

        def format_timestamp(t_str):
            if not t_str: return ""
            try:
                dt_utc = datetime.strptime(t_str[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc)
                local_dt = dt_utc.astimezone()
                diff_sec = max(0, int((now_utc - dt_utc).total_seconds()))
                time_str = local_dt.strftime('%H:%M')
                date_str = local_dt.strftime('%d.%m')
                if diff_sec < 60:
                    rel = "just now"
                elif diff_sec < 3600:
                    rel = f"{diff_sec // 60}m ago"
                elif diff_sec < 86400:
                    rel = f"{diff_sec // 3600}h ago"
                else:
                    rel = f"{diff_sec // 86400}d ago"
                return f"{date_str} {time_str} ({rel})"
            except Exception:
                return t_str[:16]

        for cid, s in summaries.items():
            title = s.get("summary") or s.get("annotations", {}).get("title") or f"Session {cid[:8]}"
            workspaces = [w.get("workspaceFolderAbsoluteUri", "") for w in s.get("workspaces", [])]
            ws_name = "Workspace"
            if workspaces and workspaces[0]:
                decoded = urllib.parse.unquote(workspaces[0])
                ws_name = decoded.replace('file:///', '').replace('/', '\\').split('\\')[-1]

            traj = self.client.rpc("GetCascadeTrajectory", {"cascadeId": cid})
            t_obj = traj.get("trajectory", {}) if traj else {}
            gm_list = t_obj.get("generatorMetadata", [])

            total_input, total_output, total_thinking, total_cache = 0, 0, 0, 0
            model_counts = {}

            for gm in gm_list:
                cm = gm.get("chatModel", {})
                raw_id = cm.get("model", "")
                mname = model_map.get(raw_id, raw_id)
                if not mname or mname.startswith('MODEL_'):
                    mname = 'Gemini 3.8 Flash (Medium)'

                usage = cm.get("usage", {})
                inp = int(usage.get("inputTokens", 0) or 0)
                out = int(usage.get("outputTokens", 0) or 0)
                th = int(usage.get("thinkingOutputTokens", 0) or 0)
                ca = int(usage.get("cacheReadTokens", 0) or 0)

                total_input += inp
                total_output += out
                total_thinking += th
                total_cache += ca
                overall_calls += 1

                if mname not in model_counts:
                    model_counts[mname] = {"calls": 0, "input": 0, "output": 0, "thinking": 0, "cache": 0, "total": 0}
                model_counts[mname]["calls"] += 1
                model_counts[mname]["input"] += inp
                model_counts[mname]["output"] += out
                model_counts[mname]["thinking"] += th
                model_counts[mname]["cache"] += ca
                model_counts[mname]["total"] += (inp + out)

                if mname not in overall_models:
                    overall_models[mname] = {"calls": 0, "input": 0, "output": 0, "thinking": 0, "cache": 0, "total": 0}
                overall_models[mname]["calls"] += 1
                overall_models[mname]["input"] += inp
                overall_models[mname]["output"] += out
                overall_models[mname]["thinking"] += th
                overall_models[mname]["cache"] += ca
                overall_models[mname]["total"] += (inp + out)

            overall_input += total_input
            overall_output += total_output
            overall_thinking += total_thinking
            overall_cache += total_cache

            results.append({
                "id": cid,
                "title": title,
                "workspace": ws_name,
                "stepCount": s.get("stepCount", 0),
                "createdTime": format_timestamp(s.get("createdTime", "")),
                "lastModifiedTime": format_timestamp(s.get("lastModifiedTime", "")),
                "totalInputTokens": total_input,
                "totalOutputTokens": total_output,
                "totalThinkingTokens": total_thinking,
                "totalCacheTokens": total_cache,
                "totalTokens": total_input + total_output,
                "models": model_counts
            })

        results.sort(key=lambda x: x["totalTokens"], reverse=True)

        return {
            "totalConversations": len(results),
            "totalTokens": overall_input + overall_output,
            "totalInputTokens": overall_input,
            "totalOutputTokens": overall_output,
            "totalThinkingTokens": overall_thinking,
            "totalCacheTokens": overall_cache,
            "totalCalls": overall_calls,
            "conversations": results,
            "modelsSummary": overall_models
        }
