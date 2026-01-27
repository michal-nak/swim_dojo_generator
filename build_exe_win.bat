# Windows Executable Build Script for Swim Dojo Generator
# This script uses PyInstaller to create a standalone .exe for gui.py
# Run this script in a Windows environment with Python 3.x installed

# Install required packages
pip install --upgrade pip
pip install pyinstaller requests beautifulsoup4

# Build the executable (no console window, GUI only)
pyinstaller --noconsole --onefile --name "SwimDojoGenerator" gui.py

# The .exe will be in the 'dist' folder

echo Build complete. The executable is located in the dist folder as SwimDojoGenerator.exe.
pause
