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
./tools/sliver/kill_multiplayermod.sh 1234
echo "Prepare success!"

# Run
rm -rf ./data/payloads/win_stager.c
rm -rf ./data/payloads/win_runner.c
rm -rf ./data/payloads/win_runner.exe
# ./tools/sliver/get_configs.sh
# ./tools/sliver/get_stagers.sh
./tools/sliver/auto.sh
