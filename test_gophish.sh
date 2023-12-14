#!/bin/bash

# Check if gophish module is installed
if ! python3 -c "import gophish" 2>/dev/null; then
    echo "gophish module not found. Installing..."
    pip install gophish
fi

# Run your Python script
python3 tools/gophish/custom_gophish.py
