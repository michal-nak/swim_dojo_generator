# Swim Dojo Workout Generator - PowerShell Launcher
# Alternative to .bat file for users with PowerShell

Write-Host "========================================"
Write-Host " Swim Dojo Workout Generator"
Write-Host "========================================"
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Python not found"
    }
    Write-Host "Python detected: $pythonVersion"
    Write-Host ""
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python from: https://www.python.org/downloads/"
    Write-Host "Make sure to check 'Add Python to PATH' during installation."
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if requirements are already installed
Write-Host "Checking dependencies..."
$requirementsInstalled = $false
try {
    python -c "import requests; import bs4" 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        $requirementsInstalled = $true
    }
} catch {
    $requirementsInstalled = $false
}

if (-not $requirementsInstalled) {
    Write-Host "Installing required packages..."
    Write-Host "This may take a minute..."
    
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "ERROR: Failed to install dependencies!" -ForegroundColor Red
        Write-Host "Please check your internet connection and try again."
        Write-Host ""
        Read-Host "Press Enter to exit"
        exit 1
    }
    
    Write-Host ""
    Write-Host "Dependencies installed successfully!" -ForegroundColor Green
} else {
    Write-Host "All dependencies are already installed!" -ForegroundColor Green
}

Write-Host ""
Write-Host "Starting Swim Workout Generator..."
Write-Host ""

# Run the GUI application
python swim_workout_gui.py

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "An error occurred." -ForegroundColor Red
    Read-Host "Press Enter to close"
}
