#!/usr/bin/env python3
"""
Cross-platform launcher for Swim Workout Generator
Checks dependencies and launches the GUI application
"""

import sys
import subprocess
import os


def check_python_version():
    """Check if Python version is adequate"""
    if sys.version_info < (3, 7):
        print("ERROR: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True


def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import requests
        import bs4
        print("✓ All dependencies installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e.name}")
        return False


def install_dependencies():
    """Install required dependencies"""
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies")
        return False


def launch_gui():
    """Launch the GUI application"""
    print("\nLaunching Swim Workout Generator...\n")
    try:
        subprocess.run([sys.executable, "swim_workout_gui.py"])
    except KeyboardInterrupt:
        print("\nApplication closed by user")
    except Exception as e:
        print(f"\n✗ Error launching application: {e}")
        return False
    return True


def main():
    """Main launcher function"""
    print("=" * 50)
    print(" Swim Dojo Workout Generator Launcher")
    print("=" * 50)
    print()
    
    # Check Python version
    if not check_python_version():
        input("\nPress Enter to exit...")
        return 1
    
    # Check dependencies
    if not check_dependencies():
        response = input("\nInstall missing dependencies? (y/n): ").strip().lower()
        if response in ('y', 'yes'):
            if not install_dependencies():
                input("\nPress Enter to exit...")
                return 1
            print()
        else:
            print("Cannot run without dependencies")
            input("\nPress Enter to exit...")
            return 1
    
    # Launch GUI
    if not launch_gui():
        input("\nPress Enter to exit...")
        return 1
    
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nLauncher interrupted by user")
        sys.exit(0)
