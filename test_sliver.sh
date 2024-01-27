#!/bin/bash

# Set execute permissions for Sliver scripts
find ./tools/sliver/ -name "*.sh" -type f -exec chmod +x {} \;
echo "Execute permission set for all Sliver scripts"

# Set execute permissions for Apache2 scripts
find ./tools/apache2/ -name "*.sh" -type f -exec chmod +x {} \;
echo "Execute permission set for all Apache2 scripts"

# Prepare - clean folder + kill old process + create payload
## Clean folder
./tools/sliver/clear_configs.sh
./tools/apache2/clear_configs.sh
echo "Clean relative folder success!"

## Kill old multiplayer mode in previous sliver-server
./tools/sliver/kill_multiplayermod.sh 31337
echo "Prepare success!"git p

# Run
./tools/sliver/get_configs.sh
