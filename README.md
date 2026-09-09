# apogee-antigravity-manager

A lightweight local status dashboard and account switcher for Google Antigravity IDE.

## Overview

Antigravity IDE runs a background language server (`language_server.exe`) that enforces rate limits and quota buckets across Gemini and third-party models (Claude, GPT). This dashboard connects to the local RPC service, extracts current quota windows, tracks token consumption per session, and enables fast switching between Google accounts without restarting the IDE.

## Features

- **Live Quotas**: Queries the local language server for true weekly and 5-hour session quota buckets.
- **Model Detection**: Inspects active cascade trajectories to display the model currently engaged in your editor session.
- **Token Telemetry**: Aggregates token usage (prompt, completion, thinking, cached context) across past conversation trajectories with local timestamps.
- **Account Management**: Integrates with Windows Credential Manager and local storage to switch accounts or authorize new Google profiles via OAuth.
- **RPC Reset**: Cleanly respawns the language server process if the local RPC connection becomes unresponsive.
- **Zero Dependencies**: Pure Python standard library implementation (`urllib`, `http.server`, `ctypes`, `json`, `ssl`).

## Prerequisites

- Windows 10/11 (macOS / Linux support for trajectory inspection)
- Python 3.8+
- Antigravity IDE (standard installation or portable)

## Quickstart

### Windows
Double-click `run.bat` or run from terminal:
```cmd
python server.py
```

The web dashboard will automatically open at:
```
http://127.0.0.1:28888/
```

### Options
```text
usage: server.py [-h] [--port PORT] [--host HOST] [--no-browser]

options:
  --port PORT     Server port (default: 28888)
  --host HOST     Host address (default: 127.0.0.1)
  --no-browser    Do not open browser on startup
```

## Architecture

```text
apogee-antigravity-manager/
├── server.py              # CLI entrypoint and HTTP API server
├── core/
│   ├── client.py          # Language Server RPC & gRPC-web protocol client
│   ├── accounts.py        # Windows Credential Manager ctypes wrapper & OAuth
│   └── telemetry.py       # Trajectory parser and token aggregator
├── web/
│   ├── index.html         # Web dashboard markup
│   ├── css/style.css      # Stylesheet
│   ├── js/app.js          # Dashboard client logic and I18N
│   └── assets/            # Vector brand assets
├── run.bat                # Windows launcher script
├── run.sh                 # Unix launcher script
└── pyproject.toml
```

## License

MIT
