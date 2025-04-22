@echo off
title ConanModpackManager - By DJRLincs
setlocal EnableDelayedExpansion

:: Script Description
echo.
echo Checking for Python installation:
py -3 --version 2>nul
echo.
echo This script will check for Python, install it if not found, and then run the ConanModpackManager script.
echo **NOTE**: This is a run everytime you want to do it. If you wish to automate it for when you open the conan 
echo launcher, please feel free to help contribute to the project.
echo.
echo.

:: Automation flag check
if /I "%1"=="/auto" goto :CHECK_PYTHON

:: Prompt user to proceed
:PROMPT
set /P AREYOUSURE=Are you sure you wish to run the script (Y/N)? 
if /I "!AREYOUSURE!" NEQ "Y" goto :END

:CHECK_PYTHON
:: Check if Python is installed
py -3 --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    cls
    echo Python is not installed or not in PATH! If you confirm, Winget will install Python 3.10.2 for you.
    echo Otherwise, the script will exit without running.
    echo.
    if /I "%1"=="/auto" (
        set INSTALL_CONFIRM=Y
    ) else (
        choice /C YN /M "Press Y to install Python, or N to cancel and exit."
        if !ERRORLEVEL! EQU 2 goto :END
        if !ERRORLEVEL! EQU 1 set INSTALL_CONFIRM=Y
    )
    if "!INSTALL_CONFIRM!"=="Y" (
        echo Installing Python via Winget...
        winget install -e --id Python.Python.3.10 -v 3.10.2 --scope machine --override "/quiet InstallAllUsers=1 PrependPath=1"
        if !ERRORLEVEL! NEQ 0 (
            echo ERROR: Python installation failed. Possible causes: no internet or Microsoft Store issues.
            echo Please install Python manually: https://www.python.org/downloads/release/python-3102/
            echo **Important**: Check "Add Python to PATH" during manual installation.
            pause
            goto :END
        )
        echo.
        echo Python installation complete. You may need to restart your machine if Python isn't recognized in PATH.
    )
)

:: Run the Python script
echo Running ConanModpackManager script...
py ConanModpackSelector.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to run ConanModpackSelector.py. Please check the script for errors.
    echo Try running 'py ConanModpackSelector.py' manually to diagnose.
    pause
)

:END
echo.
echo Script execution complete.
if /I not "%1"=="/auto" pause
exit