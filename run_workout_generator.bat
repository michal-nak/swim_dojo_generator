@echo off
REM Swim Dojo Workout Generator - Windows Launcher
REM This script automatically sets up and runs the Swim Workout Generator

echo ========================================
echo  Swim Dojo Workout Generator
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo Python detected:
python --version
echo.

REM Check if requirements are already installed
echo Checking dependencies...
python -c "import requests; import bs4" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    echo This may take a minute...
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install dependencies!
        echo Please check your internet connection and try again.
        echo.
        pause
        exit /b 1
    )
    echo.
    echo Dependencies installed successfully!
) else (
    echo All dependencies are already installed!
)

echo.
echo Starting Swim Workout Generator...
echo.

REM Run the GUI application
python swim_workout_gui.py

REM Keep window open if there was an error
if errorlevel 1 (
    echo.
    echo An error occurred. Press any key to close...
    pause >nul
)
