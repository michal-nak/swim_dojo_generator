# Swim Dojo Workout Generator 🏊

Generate random swim workouts from [SwimDojo.com](https://www.swimdojo.com) with an easy-to-use graphical interface!

Based on the concept from: https://www.reddit.com/r/Swimming/comments/1dtzus8/i_made_a_script_that_opens_a_random_swim_workout/

## Features

- 🎯 Simple graphical user interface (GUI)
- 🏷️ Filter workouts by tags (sprint, endurance, technique, etc.)
- 🎲 Random workout selection
- 🌐 Opens workouts directly in your browser
- 💻 Easy Windows installation - no coding required!

## Quick Start (Windows Users)

### For Users Who Don't Know How to Code:

1. **Install Python** (if not already installed):
   - Download from: https://www.python.org/downloads/
   - **IMPORTANT**: During installation, check the box "Add Python to PATH"
   - Click "Install Now"

2. **Download this repository**:
   - Click the green "Code" button at the top of this page
   - Select "Download ZIP"
   - Extract the ZIP file to a folder on your computer

3. **Run the application**:
   - Double-click `run_workout_generator.bat`
   - That's it! The app will automatically install dependencies and launch

### Alternative: Manual Setup

If you prefer to set up manually:

1. Open Command Prompt in the project folder
2. Run: `setup.bat`
3. Then run: `run_workout_generator.bat`

## Usage

1. Launch the application using `run_workout_generator.bat`
2. (Optional) Select a specific workout type from the dropdown
3. Click "Get Random Workout!" 
4. A random workout will open in your default web browser
5. Enjoy your swim training!

## Files Included

- `swim_workout_fetcher.py` - Core script to fetch workouts from SwimDojo.com
- `swim_workout_gui.py` - Graphical user interface
- `run_workout_generator.bat` - Easy launcher for Windows (auto-installs dependencies)
- `setup.bat` - First-time setup script
- `requirements.txt` - Python package dependencies

## Requirements

- Python 3.7 or higher
- Internet connection
- Dependencies (automatically installed):
  - requests
  - beautifulsoup4

## For Developers

### Running from Command Line

```bash
# Install dependencies
pip install -r requirements.txt

# Run the GUI
python swim_workout_gui.py

# Or run the command-line version
python swim_workout_fetcher.py
```

### Running Tests

```bash
# Test the core fetcher
python swim_workout_fetcher.py
```

## Troubleshooting

**Problem**: "Python is not recognized..."
- **Solution**: Python is not installed or not in PATH. Reinstall Python and check "Add Python to PATH"

**Problem**: Application won't start
- **Solution**: Try running `setup.bat` first, then `run_workout_generator.bat`

**Problem**: No workouts found
- **Solution**: Check your internet connection and try again

**Problem**: Dependencies won't install
- **Solution**: Make sure you have an internet connection. Try running: `python -m pip install --upgrade pip` first

## License

This project is licensed under the MIT License - see the LICENSE file for details.
