@echo off
REM mhkji wrapper for Windows — uses the Python launcher (py) to run mhkji.py
REM Usage: .\mhkji.bat arg1 arg2 ...

SETLOCAL ENABLEDELAYEDEXPANSION
REM Resolve the script directory and run mhkji.py with provided args
SET SCRIPT_DIR=%~dp0
py -3 "%SCRIPT_DIR%mhkji.py" %*
ENDLOCAL
