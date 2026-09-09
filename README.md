# Apogee — Antigravity Manager

[![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-3b82f6?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-64748b?style=flat-square)](LICENSE)
[![Dependencies](https://img.shields.io/badge/dependencies-zero%20(stdlib%20only)-10b981?style=flat-square)](pyproject.toml)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-475569?style=flat-square)](server.py)

A lightweight local status dashboard, quota monitor, and multi-account switcher for Google Antigravity IDE.

---

### The Problem

Google Antigravity runs a local background language server (`language_server.exe`) that mediates all interactions with Gemini and third-party frontier models (Claude Opus/Sonnet, GPT-OSS). Rate limits are enforced on both rolling weekly windows and 5-hour session buckets, but the editor UI provides minimal visibility into exact percentage depletion, reset countdowns, or token burn rates across agent cascades.

**Apogee** runs locally as a companion dashboard with **zero external dependencies** (pure Python standard library). It connects directly to the Language Server's local RPC interface, tracks quota windows, displays per-session token telemetry, and allows hot-switching active models and Google profiles on the fly.

---

## Screenshots

### Live Quotas & Sliding Windows
*Real-time weekly and 5-hour quota pools queried directly from Language Server RPC.*
![Dashboard](docs/screenshots/dashboard.png)

### Model Catalog & Hot-Switching
*Individual model status, remaining percentages, and one-click active agent model selection.*
![Catalog](docs/screenshots/catalog.png)

### Session Token Telemetry
*Granular breakdown of prompt, completion, thinking tokens, and cache savings across workspace tasks.*
![Telemetry](docs/screenshots/telemetry.png)

---

## Features

| Capability | Detail |
|---|---|
| **Live Quota Windows** | Queries `RetrieveUserQuotaSummary` and `GetUserStatus` over gRPC-web for exact weekly and 5h limits. |
| **Model Hot-Switching** | Select any available model (Claude 4.6, GPT-OSS 120B, Gemini 3.8/3.7/3.1) with immediate state file persistence. |
| **Token Accounting** | Aggregates prompt, completion, reasoning/thinking, and context cache read tokens from conversation trajectories. |
| **Multi-Account Switching** | Integrates with Windows Credential Manager (`wincred.dll` via `ctypes`) and OAuth to swap Google profiles cleanly. |
| **RPC Watchdog** | Detects hung language server processes and offers a clean one-click restart without restarting the entire IDE. |
| **Zero Dependencies** | Implemented strictly with standard library modules (`http.server`, `urllib`, `ctypes`, `json`, `ssl`, `sqlite3`). |

---

## Quickstart

### Prerequisites
- Python 3.8 or higher
- Antigravity IDE (standard installation or portable)
- Windows 10/11 (macOS / Linux supported for trajectory inspection)

### Windows
Double-click `run.bat` or run:
```cmd
python server.py
```

### Linux / macOS
```bash
chmod +x run.sh
./run.sh
```

The web dashboard will automatically open at:
```
http://127.0.0.1:28888/
```

### Command Line Options

```text
usage: server.py [-h] [--port PORT] [--host HOST] [--no-browser]

options:
  --port PORT     Server port (default: 28888)
  --host HOST     Host address (default: 127.0.0.1)
  --no-browser    Do not open browser automatically on startup
```

---

## Keyboard Shortcuts

The dashboard supports full keyboard navigation for fast multi-tasking:

| Shortcut | Action |
|---|---|
| `1` | Switch to **Quotas & Limits** |
| `2` | Switch to **Model Catalog** |
| `3` | Switch to **Token Telemetry** |
| `4` | Switch to **Google Profiles & Settings** |
| `/` | Focus model search input |
| `R` | Force refresh all metrics from RPC |

---

## How It Works

1. **Dynamic Port Probing**: Antigravity IDE launches `language_server.exe` with `--https_server_port 0`, causing the OS to bind an ephemeral TCP port. Apogee locates the active process, inspects its listening sockets via `netstat`, and probes candidate ports over HTTPS to resolve the RPC endpoint.
2. **gRPC-web Protocol**: Communication with the language server uses Connect/gRPC-web with length-prefixed binary frames (`Connect-Protocol-Version: 1`, `X-Codeium-Csrf-Token`).
3. **Model Selection**: Switching a model updates `last_selected_agent_model` in `antigravity_state.pbtxt` so that subsequent agent sessions and prompts engage the chosen model.
4. **Credential Storage**: On Windows, access and refresh tokens are managed through the native Credential Manager API (`CredReadW` / `CredWriteW`), keeping credentials secure and isolated.

---

## Architecture

```text
apogee-antigravity-manager/
├── server.py              # CLI entrypoint and HTTP API server
├── core/
│   ├── client.py          # Language Server RPC & gRPC-web protocol client
│   ├── accounts.py        # Windows Credential Manager ctypes wrapper & OAuth
│   └── telemetry.py       # Trajectory parser and token aggregator
├── docs/
│   └── screenshots/       # High-DPI UI preview captures
├── web/
│   ├── index.html         # Dashboard markup
│   ├── css/style.css      # Dark-mode stylesheet
│   ├── js/app.js          # Client-side state, event handlers & i18n
│   └── assets/            # Vector logos (Gemini, Claude, OpenAI)
├── run.bat                # Windows quickstart launcher
├── run.sh                 # Unix quickstart launcher
├── requirements.txt       # Development dependencies (optional)
└── pyproject.toml         # Package metadata and tool configurations
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.
