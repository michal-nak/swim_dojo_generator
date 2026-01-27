@echo off
REM Creates a desktop shortcut for the Swim Workout Generator

echo ========================================
echo  Create Desktop Shortcut
echo ========================================
echo.

REM Get the current directory
set SCRIPT_DIR=%~dp0

REM Get the desktop path
set DESKTOP=%USERPROFILE%\Desktop

REM Create a VBScript to create the shortcut
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "%DESKTOP%\Swim Workout Generator.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%SCRIPT_DIR%run_workout_generator.bat" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "%SCRIPT_DIR%" >> CreateShortcut.vbs
echo oLink.Description = "Swim Dojo Workout Generator" >> CreateShortcut.vbs
echo oLink.IconLocation = "C:\Windows\System32\imageres.dll,117" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs

REM Execute the VBScript
cscript CreateShortcut.vbs

REM Delete the VBScript
del CreateShortcut.vbs

echo.
echo ========================================
echo Shortcut created on your Desktop!
echo ========================================
echo.
echo You can now launch the Swim Workout Generator
echo from the "Swim Workout Generator" shortcut
echo on your Desktop.
echo.
pause
