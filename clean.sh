#!/bin/bash

# Set execute permissions for Sliver scripts
find ./tools/sliver/ -name "*.sh" -type f -exec chmod +x {} \;
echo "Execute permission set for all Sliver scripts"

# Set execute permissions for Apache2 scripts
find ./tools/apache2/ -name "*.sh" -type f -exec chmod +x {} \;
echo "Execute permission set for all Apache2 scripts"

# clear all

./tools/sliver/clear_configs.sh
./tools/apache2/clear_configs.sh
