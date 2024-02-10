#!/bin/bash

# Change to the directory of the script
cd "$(dirname "$0")" || exit

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

echo "Setup complete. Virtual environment created and dependencies installed."
