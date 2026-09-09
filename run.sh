#!/bin/sh
cd "$(dirname "$0")"
if command -v python3 >/dev/null 2>&1; then
    exec python3 server.py "$@"
elif command -v python >/dev/null 2>&1; then
    exec python server.py "$@"
else
    echo "Python 3 is required but not found in PATH." >&2
    exit 1
fi
