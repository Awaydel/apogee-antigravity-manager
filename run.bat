@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python server.py %*
    goto :eof
)

where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    py -3 server.py %*
    goto :eof
)

echo [ERROR] Python 3 was not found in PATH.
echo Please install Python 3.8+ from https://www.python.org/
pause
