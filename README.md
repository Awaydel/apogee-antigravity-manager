<p align="center">
  <br>
  <pre align="center">
<b>
   █████╗ ██████╗  ██████╗  ██████╗ ███████╗███████╗
  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔════╝██╔════╝
  ███████║██████╔╝██║   ██║██║  ███╗█████╗  █████╗  
  ██╔══██║██╔═══╝ ██║   ██║██║   ██║██╔══╝  ██╔══╝  
  ██║  ██║██║     ╚██████╔╝╚██████╔╝███████╗███████╗
  ╚═╝  ╚═╝╚═╝      ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
</b>
  </pre>
  <h1 align="center">Apogee — Antigravity Manager</h1>
  <p align="center">
    <strong>Zero-dependency local dashboard, real-time quota telemetry & multi-account switcher for Google Antigravity IDE.</strong>
  </p>
  <p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-64748b?style=flat-square&labelColor=0f172a" alt="License: MIT"></a>
    <img src="https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-3b82f6?style=flat-square&labelColor=0f172a&logo=python&logoColor=white" alt="Python 3.8+">
    <img src="https://img.shields.io/badge/dependencies-zero%20(stdlib%20only)-10b981?style=flat-square&labelColor=0f172a" alt="Zero Dependencies">
    <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-475569?style=flat-square&labelColor=0f172a" alt="Platforms">
    <img src="https://img.shields.io/badge/telemetry-100%25%20local%20RPC-8b5cf6?style=flat-square&labelColor=0f172a" alt="Local RPC">
  </p>
  <p align="center">
    <a href="#-the-problem">The Problem</a> •
    <a href="#-screenshots">Screenshots</a> •
    <a href="#-key-features">Key Features</a> •
    <a href="#-quickstart">Quickstart</a> •
    <a href="#-keyboard-shortcuts">Shortcuts</a> •
    <a href="#-how-it-works">How It Works</a> •
    <a href="#-architecture">Architecture</a>
  </p>
</p>

---

## ⚡ The Problem

Google Antigravity coordinates language models through a background RPC daemon (`language_server.exe`). Rate limits are enforced on both rolling weekly pools and 5-hour velocity windows across Gemini, Claude (Opus / Sonnet 4.6), and OpenAI (GPT-OSS). 

Because the editor interface hides exact remaining percentages and token depletion curves, developers frequently hit rate limits mid-task without warning.

**Apogee** solves this by running as a local, zero-dependency companion:
1. **True Quota Depletion**: Queries `language_server.exe` via gRPC-web for exact weekly and 5h quota fractions.
2. **Model Hot-Switching**: Instantly switches the active agent model in `antigravity_state.pbtxt` without restarting the IDE.
3. **Session Token Accounting**: Parses conversation trajectories to show exact prompt, output, thinking, and cache savings per task.
4. **Multi-Account Switching**: Interops with Windows Credential Manager (`wincred.dll` via `ctypes`) and OAuth2 to swap Google accounts in seconds.

---

## 📸 Screenshots

### 1. Live Quotas & Sliding Windows
*Real-time weekly and 5-hour quota pools queried directly from Language Server RPC.*
<p align="center">
  <img src="docs/screenshots/dashboard.png" alt="Apogee Quota Dashboard" width="960" style="border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.5);">
</p>

### 2. Model Catalog & Hot-Switching
*Individual model status, remaining percentages, and one-click active agent model selection.*
<p align="center">
  <img src="docs/screenshots/catalog.png" alt="Apogee Model Catalog" width="960" style="border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.5);">
</p>

### 3. Session Token Telemetry
*Granular breakdown of prompt, completion, thinking tokens, and cache savings across workspace tasks.*
<p align="center">
  <img src="docs/screenshots/telemetry.png" alt="Apogee Token Telemetry" width="960" style="border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.5);">
</p>

---

## ⚡ Key Features

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>◈ Live Quota Tracking</h3>
      <ul>
        <li><b>Zero Synthetic Data:</b> 100% genuine RPC polling via <code>RetrieveUserQuotaSummary</code>.</li>
        <li><b>Sliding Windows:</b> Independent weekly & 5-hour rate-limit meters.</li>
        <li><b>Reset Timers:</b> Live second-by-second countdown to quota replenishment.</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>◈ Model Management</h3>
      <ul>
        <li><b>One-Click Selection:</b> Switch active model across Gemini, Claude, and GPT-OSS.</li>
        <li><b>State Sync:</b> Updates <code>antigravity_state.pbtxt</code> immediately on disk.</li>
        <li><b>Filter Chips:</b> Instant filtering by provider (Google, Anthropic, OpenAI) or reasoning/thinking.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>◈ Token Accounting</h3>
      <ul>
        <li><b>Telemetry Engine:</b> Tracks prompt, output, thinking, and cache reads per conversation.</li>
        <li><b>Task Attribution:</b> See which workspace task consumed your rate limits.</li>
        <li><b>Consumption Ratio:</b> Visual breakdown of token usage across models.</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>◈ Security & Multi-Profile</h3>
      <ul>
        <li><b>Windows Credential Manager:</b> Native <code>wincred.dll</code> ctypes integration.</li>
        <li><b>OAuth2 Auth Flow:</b> Connect multiple Google accounts securely.</li>
        <li><b>RPC Process Watchdog:</b> Clean one-click respawn for unresponsive language server processes.</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🚀 Quickstart

Apogee requires **zero external pip dependencies** — it runs entirely on the standard Python 3.8+ library.

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

### CLI Arguments

```text
usage: server.py [-h] [--port PORT] [--host HOST] [--no-browser]

options:
  --port PORT     Server port (default: 28888)
  --host HOST     Host address (default: 127.0.0.1)
  --no-browser    Do not open browser automatically on startup
```

---

## ⌨️ Keyboard Shortcuts

Apogee supports full single-key navigation:

| Key | Action |
|:---:|:---|
| `1` | Switch to **Quotas & Velocity Limits** tab |
| `2` | Switch to **Model Catalog & Switching** tab |
| `3` | Switch to **Token Telemetry** tab |
| `4` | Switch to **Google Profiles & Component Controls** tab |
| `/` | Instant focus into Model Search box |
| `R` | Force refresh all metrics from Language Server RPC |

---

## ⚙️ How It Works

1. **Ephemeral Port Discovery**: Antigravity IDE launches `language_server.exe` with `--https_server_port 0`. Apogee detects the process PID, queries active listening sockets via `netstat`, and validates the HTTPS RPC port automatically.
2. **gRPC-web Length-Prefixed Unmarshalling**: Apogee speaks native Connect/gRPC-web protocol with 5-byte frame prefixes (`Connect-Protocol-Version: 1`, `X-Codeium-Csrf-Token`).
3. **Model Selection Persistence**: Selecting a model writes `last_selected_agent_model` to `antigravity_state.pbtxt`, ensuring subsequent agent sessions initialize with the chosen model.
4. **Credential Isolation**: On Windows, authentication tokens are read and written using Windows Credential Manager (`CredReadW` / `CredWriteW`), avoiding plaintext disk storage.

---

## 🏛️ Architecture

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
├── LICENSE                # MIT License
├── requirements.txt       # Optional dev dependencies
└── pyproject.toml         # Packaging metadata
```

---

## 📄 License

Distributed under the [MIT License](LICENSE).
