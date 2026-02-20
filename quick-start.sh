#!/bin/bash

# Nexios Bootstrap Quick Start Script for Linux/macOS
# One-liner: curl -sSL https://raw.githubusercontent.com/nexios-labs/nexios-bootstrap/main/quick-start.sh | bash

set -e

echo "🚀 Starting Nexios Bootstrap setup..."

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Detect OS and package manager
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    if command_exists brew; then
        PKG_MANAGER="brew"
        PYTHON_CMD="python3"
    else
        echo "❌ Homebrew not found. Please install it first: https://brew.sh/"
        exit 1
    fi
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if command_exists apt-get; then
        PKG_MANAGER="apt"
        PYTHON_CMD="python3"
    elif command_exists yum; then
        PKG_MANAGER="yum"
        PYTHON_CMD="python3"
    elif command_exists dnf; then
        PKG_MANAGER="dnf"
        PYTHON_CMD="python3"
    else
        echo "❌ Unsupported package manager. Please install Python 3.10+ manually."
        exit 1
    fi
else
    echo "❌ Unsupported OS: $OSTYPE"
    exit 1
fi

# Check Python version
if ! command_exists $PYTHON_CMD; then
    echo "📦 Installing Python..."
    case $PKG_MANAGER in
        brew)
            brew install python
            ;;
        apt)
            sudo apt update && sudo apt install -y python3 python3-pip python3-venv
            ;;
        yum|dnf)
            sudo $PKG_MANAGER install -y python3 python3-pip
            ;;
    esac
fi

# Check Python version compatibility
PYTHON_VERSION=$($PYTHON_CMD -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $PYTHON_VERSION found. Nexios requires Python $REQUIRED_VERSION or higher."
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"

# Install uv if not present
if ! command_exists uv; then
    echo "📦 Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Create project directory
PROJECT_DIR="nexios-app"
if [ -d "$PROJECT_DIR" ]; then
    echo "📁 Directory $PROJECT_DIR already exists. Removing it..."
    rm -rf "$PROJECT_DIR"
fi

echo "📥 Cloning Nexios Bootstrap..."
git clone https://github.com/nexios-labs/nexios-bootstrap.git "$PROJECT_DIR"
cd "$PROJECT_DIR"

echo "📦 Installing dependencies with uv..."
uv pip install -r requirements.txt

echo "🔧 Setting up environment..."
if [ ! -f ".env" ]; then
    cp .env.example .env
fi

# Find available port
PORT=8000
while lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; do
    PORT=$((PORT + 1))
done

echo "🌐 Starting server on port $PORT..."
echo "📱 Opening browser..."

# Open browser based on OS
case $OSTYPE in
    darwin*)
        open http://localhost:$PORT/health/
        ;;
    linux-gnu*)
        if command_exists xdg-open; then
            xdg-open http://localhost:$PORT/health/
        elif command_exists gnome-open; then
            gnome-open http://localhost:$PORT/health/
        else
            echo "🌐 Please open http://localhost:$PORT/health/ in your browser"
        fi
        ;;
esac

# Start the server
echo "🚀 Server starting at http://localhost:$PORT"
echo "📊 Health check: http://localhost:$PORT/health/"
echo "🛑 Press Ctrl+C to stop the server"

# Run the application
$PYTHON_CMD -m src.main
