@echo off
title ConanModpackManager - By DJRLincs
echo.
echo Checking for Python installation:
py -3 --version

echo.
echo This script will check for Python, install it if its not found, and then run the ConanModpackManager script.
echo **NOTE**: This is a run everytime you want to do it. If you wish to automate it for when you open the conan 
echo launcher, please feel free to help contribute to the project.
echo.
echo.

:PROMPT
SET /P AREYOUSURE=Are you sure you wish to run the script (Y/N)? 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

:: Check if Python is installed by running `py -3 --version`. If not, attempt installation via Winget
py -3 --version
IF %ERRORLEVEL% NEQ 0 (
  cls
  echo Python is not installed or not in PATH! If you confirm, Winget will install Python 3.10.2 for you.
  echo Otherwise, the script will exit without running.
  echo.
  CHOICE /C YN /M "Press Y to install Python, or N to cancel and exit."
  
  IF ERRORLEVEL 2 GOTO END
  IF ERRORLEVEL 1 (
    echo Installing Python via Winget...
    winget install -e --id=Python.Python.3.10 -v "3.10.2" --scope=machine
    echo.
    echo Python installation complete. You may need to restart your machine if Python isn’t recognized in PATH immediately.
    echo If needed, download manually from: https://www.python.org/downloads/release/python-3102/
    echo **Important**: During installation, check the box for "Add Python to PATH."
    pause
  )
)

:: Run the Python script for ConanModpackManager
echo Running ConanModpackManager script...
py ConanModpackSelector.py

pause
:END
exit
