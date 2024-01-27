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
set_execute_permission "./tools/sliver/*.sh"
# set_execute_permission "./tools/sliver/custom_sliver.sh"
# set_execute_permission "./tools/sliver/clear_configs.sh"
# set_execute_permission "./tools/sliver/get_config.sh"
# set_execute_permission "./tools/sliver/active_server.sh"

# Set execute permissions for Apache2 script
set_execute_permission "./tools/apache2/custom_apache2.sh"

# Kill old multiplayer mod
./tools/sliver/kill_multiplayermod.sh

# ./tools/spiderfoot/emails_from_domain.sh -d "hcmus.edu.vn" -o "emails_hcmus_edu_vn.txt" -r "./data/emails"
# ./tools/sliver/get_config.sh