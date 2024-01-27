#!/bin/bash

# Function to set execute permission on a file
set_execute_permission() {
    if [ -x "$1" ]; then
        echo "Execute permission already set for $1"
    else
        chmod +x "$1"
        echo "Execute permission set for $1"
    fi
}

# Set execute permissions for Sliver scripts
set_execute_permission "./tools/sliver/clear_configs.sh"
set_execute_permission "./tools/apache2/clear_configs.sh"

# clear all

./tools/sliver/clear_configs.sh
./tools/apache2/clear_configs.sh