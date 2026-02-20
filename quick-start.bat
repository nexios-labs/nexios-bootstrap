@echo off
REM Nexios Bootstrap Quick Start Script for Windows
REM One-liner: powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/nexios-labs/nexios-bootstrap/main/quick-start.bat' | Invoke-Expression"

echo 🚀 Starting Nexios Bootstrap setup...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.10+ from https://python.org
    pause
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
if "%PYTHON_VERSION:~0,3%" LSS "3.10" (
    echo ❌ Python %PYTHON_VERSION% found. Nexios requires Python 3.10 or higher.
    pause
    exit /b 1
)

echo ✅ Python %PYTHON_VERSION% detected

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git not found. Please install Git from https://git-scm.com
    pause
    exit /b 1
)

REM Check if uv is installed
uv --version >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing uv package manager...
    powershell -Command "irm https://astral.sh/uv/install.ps1 | iex"
    if errorlevel 1 (
        echo ❌ Failed to install uv. Please install manually: https://docs.astral.sh/uv/getting-started/installation
        pause
        exit /b 1
    )
)

REM Create project directory
set PROJECT_DIR=nexios-app
if exist "%PROJECT_DIR%" (
    echo 📁 Directory %PROJECT_DIR% already exists. Removing it...
    rmdir /s /q "%PROJECT_DIR%"
)

echo 📥 Cloning Nexios Bootstrap...
git clone https://github.com/nexios-labs/nexios-bootstrap.git "%PROJECT_DIR%"
cd "%PROJECT_DIR%"

echo 📦 Installing dependencies with uv...
uv pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo 🔧 Setting up environment...
if not exist ".env" (
    copy .env.example .env
)

REM Find available port
set PORT=8000
:find_port
netstat -an | findstr ":%PORT% " >nul 2>&1
if not errorlevel 1 (
    set /a PORT+=1
    goto find_port
)

echo 🌐 Starting server on port %PORT%...
echo 📱 Opening browser...

REM Open browser
start http://localhost:%PORT%/health/

echo 🚀 Server starting at http://localhost:%PORT%
echo 📊 Health check: http://localhost:%PORT%/health/
echo 🛑 Press Ctrl+C to stop the server

REM Start the application
python -m src.main
