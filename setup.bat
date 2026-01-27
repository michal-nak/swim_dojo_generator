@echo off
REM First-time setup script for Swim Dojo Workout Generator

echo ========================================
echo  Swim Dojo Workout Generator Setup
echo ========================================
echo.
echo This will install all required dependencies.
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

echo Python version:
python --version
echo.

echo Installing required packages...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed!
    echo Please check your internet connection and try again.
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Setup Complete!
echo ========================================
echo.
echo You can now run the workout generator by:
echo   1. Double-clicking 'run_workout_generator.bat'
echo   OR
echo   2. Running: python swim_workout_gui.py
echo.
pause
