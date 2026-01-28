# Swim Dojo Workout Generator 🏊

Generate random swim workouts from [SwimDojo.com](https://www.swimdojo.com) with an easy-to-use graphical interface!

Based on the concept from: https://www.reddit.com/r/Swimming/comments/1dtzus8/i_made_a_script_that_opens_a_random_swim_workout/

## Features

- 🎯 **Simple graphical user interface (GUI)** - Easy to use, no coding required
- 🏷️ **Category-based filtering** - Filter by distance, difficulty, and style
- 🎲 **Smart intersection matching** - Get workouts matching ALL selected categories
- 🌐 **Browser integration** - Opens workouts directly in your default browser
- 💻 **Windows ready** - One-click launch with batch or PowerShell scripts
- 🖥️ **Command-line interface** - Advanced users can use CLI for automation

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
   - Double-click `run_workout_generator.bat` or `run_workout_generator.ps1`
   - The app will automatically install dependencies and launch

💡 **See QUICKSTART.md for detailed step-by-step instructions.**

## Usage

### Graphical Interface (GUI)

1. Launch the application using `run_workout_generator.bat` or `run_workout_generator.ps1`
2. Select your preferences from the dropdown menus:
   - **Distance**: Choose workout length (0-1000m, 2000-3000m, etc.) or "Any"
   - **Difficulty**: Choose intensity level (Beginner, Advanced, etc.) or "Any"
   - **Style**: Choose stroke type (Freestyle, IM, etc.) or "Any"
3. Click "Get Random Workout!"
4. A workout matching ALL your selected categories will open in your browser
5. Enjoy your swim training!

### Command-Line Interface (CLI)

```bash
# Interactive mode with category selection prompts
python randomiser.py

# Fully random workout (no filtering)
python randomiser.py --any

# Filter by specific tags
python randomiser.py Beginner Freestyle
python randomiser.py "2000-3000" Hard

# List all available tags
python randomiser.py --tags

# Show help
python randomiser.py --help
```

## How It Works

The application scrapes workout data from SwimDojo.com's archive page and allows you to filter workouts by multiple categories. When you select categories (e.g., "2000-3000m" + "Intermediate" + "Freestyle"), it finds workouts that match ALL your selections (intersection), ensuring you get exactly the type of workout you want.

## Project Structure

### Application Files
- `randomiser.py` - Core script to fetch workouts from SwimDojo.com
- `swim_workout_gui.py` - Graphical user interface
- `requirements.txt` - Python package dependencies
- `run_workout_generator.bat` - Windows launcher (batch)
- `run_workout_generator.ps1` - Windows launcher (PowerShell)

### Documentation
- `README.md` - This file (full documentation)
- `QUICKSTART.md` - Step-by-step beginner's guide
- `LICENSE` - MIT License

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
python randomiser.py
```

### Command-Line Options

The CLI supports several useful options:

```bash
# Interactive mode (prompts for category selection)
python randomiser.py

# Random workout without filtering
python randomiser.py --any

# Filter by specific tags (case-insensitive)
python randomiser.py Beginner Sprint
python randomiser.py "5000+" Advanced Freestyle

# View all available tags from swimdojo.com
python randomiser.py --tags

# Show help and usage information
python randomiser.py --help
```

### Code Structure

The codebase is organized for clarity and maintainability:

- **`randomiser.py`** - Core logic for fetching and filtering workouts
  - `open_random_workout()` - Main function to fetch workouts with tag filtering
  - `list_available_tags()` - Fetches all available tags from swimdojo.com
  - `prompt_for_tag()` - Interactive tag selection helper
  - Tag constants: `distance_tags`, `difficulty_tags`, `style_tags`

- **`swim_workout_gui.py`** - Tkinter-based GUI application
  - Category dropdown selectors
  - Status logging and error handling
  - Threaded workout fetching for responsive UI

## Troubleshooting

**Problem**: "Python is not recognized..."
- **Solution**: Python is not installed or not in PATH. Reinstall Python and check "Add Python to PATH"

**Problem**: Application won't start
- **Solution**: Make sure dependencies are installed. The launchers should handle this automatically.

**Problem**: No workouts found
- **Solution**: Check your internet connection and try again. Try selecting different categories.

**Problem**: Dependencies won't install
- **Solution**: Make sure you have an internet connection. Try running: `python -m pip install --upgrade pip` first

## License

This project is licensed under the MIT License - see the LICENSE file for details.
