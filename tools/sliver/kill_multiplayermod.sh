#!/bin/bash

# Check if a port number is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <port>"
    exit 1
fi

PORT=$1

# Check if lsof command is available
command -v lsof >/dev/null 2>&1 || { echo >&2 "lsof command not found. Aborting."; exit 1; }

# Check if any process is running on the specified port
if lsof -i :$PORT >/dev/null 2>&1; then
    # Get the PID of the process using the specified port
    PID=$(lsof -t -i :$PORT)

    # Kill the process
    kill $PID

    echo "Process with PID $PID killed on port $PORT."
else
    echo "No process found running on port $PORT."
fi
