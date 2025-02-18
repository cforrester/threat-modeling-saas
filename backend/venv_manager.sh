#!/bin/bash

# Define virtual environment directory
VENV_DIR="venv"

# Check if venv exists
if [ ! -d "$VENV_DIR" ]; then
    echo "❌ Virtual environment not found! Creating one..."
    python3 -m venv $VENV_DIR
    echo "✅ Virtual environment created."
fi

# Activate or Deactivate
if [[ "$1" == "activate" ]]; then
    echo "🔹 Activating virtual environment..."
    source $VENV_DIR/bin/activate
    echo "✅ Virtual environment activated!"
elif [[ "$1" == "deactivate" ]]; then
    echo "🔹 Deactivating virtual environment..."
    deactivate
    echo "✅ Virtual environment deactivated!"
else
    echo "Usage: ./venv_manager.sh [activate|deactivate]"
fi
