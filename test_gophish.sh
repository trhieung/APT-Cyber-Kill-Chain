#!/bin/bash

# Check if gophish module is installed
if ! python3 -c "import gophish" 2>/dev/null; then
    echo "gophish module not found. Installing..."
    pip install gophish
fi

# Check if dotenv module is installed
if ! python3 -c "import dotenv" 2>/dev/null; then
    echo "dotenv module not found. Installing..."
    pip install python-dotenv
fi

# Run your Python script
python3 tools/gophish/run_custom.py
