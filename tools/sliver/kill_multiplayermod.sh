#!/bin/bash

# Check if a port number is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <port>"
    exit 1
fi

# Port number to be killed
port="$1"

# Find the process using the specified port
pid=$(sudo lsof -t -i :$port)

if [ -z "$pid" ]; then
    echo "No process found using port $port"
else
    # Kill the process
    sudo kill -9 "$pid"
    echo "Process with PID $pid killed on port $port"
fi
