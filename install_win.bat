@echo off
REM Swim Dojo Generator Windows Installer
REM This script installs Python (if needed), pip, dependencies, and launches the app

REM Check for Python
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python not found. Downloading and installing Python 3.11. Please wait...
    powershell -Command "Start-Process 'https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe' -Wait"
    echo Please re-run this installer after Python setup completes.
    pause
    exit /b
)

REM Upgrade pip and install requirements
python -m pip install --upgrade pip
python -m pip install requests beautifulsoup4

REM Run the executable if it exists, else run the GUI script
if exist dist\SwimDojoGenerator.exe (
    start dist\SwimDojoGenerator.exe
) else (
    python gui.py
)

echo Swim Dojo Generator launched.
pause
