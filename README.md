
# swim_dojo_generator

This tool lets you easily open a random swim workout from [swimdojo.com](https://www.swimdojo.com) using a simple Windows-friendly interface. No coding or terminal knowledge required! (Or at least i tried to, first time working with windows)


## How to Use (Windows)

### Option 1: Easiest (No Python Needed)

1. **Build the Windows Executable**
		- If you downloaded this as source code, run `build_exe_win.bat` (double-click it) to create a standalone `SwimDojoGenerator.exe` in the `dist` folder. (Requires Python on your system for the build step.)
		- If you already have `SwimDojoGenerator.exe`, skip to step 2.

2. **Run the Installer**
		- Double-click `install_win.bat`.
		- This will check for Python, install it if needed, install dependencies, and launch the app.
		- If the executable exists, it will run; otherwise, it will run the GUI directly.

### Option 2: Manual (Python Required)

1. **Install Python**
		- Download and install Python 3.8 or newer from [python.org](https://www.python.org/downloads/).
		- During installation, make sure to check "Add Python to PATH".

2. **Install Requirements**
		- Open a command prompt in this folder and run:
			```
			pip install -r requirements.txt
			```

3. **Run the User Interface**
		- Double-click `gui.py` (or right-click and choose "Open with → Python").
		- Or run in a command prompt:
			```
			python gui.py
			```
		- A window will appear. Select any tags you want (or leave blank for a fully random workout) and click **Get Random Workout**.
		- Your browser will open a random workout from swimdojo.com.


## Troubleshooting

- If double-clicking `install_win.bat` or `gui.py` doesn't work, open a command prompt in this folder and run:
	```
	python gui.py
	```
- If you get errors about missing modules, repeat the install steps above.

## About
Generates a random workout based on the swimdojo website, working with tags. Based on the code of https://www.reddit.com/r/Swimming/comments/1dtzus8/i_made_a_script_that_opens_a_random_swim_workout/
