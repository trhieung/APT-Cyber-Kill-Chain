#!/bin/bash

# Set execute permissions for Spiderfoot scripts
find ./tools/spiderfoot/ -name "*.sh" -type f -exec chmod +x {} \;
echo "Execute permission set for all Spiderfoot scripts"

# Run
./tools/spiderfoot/emails_from_domain.sh -d "danck12.github.io" -o "APT.txt" -r "./data/emails"
# ./tools/spiderfoot/emails_from_domain.sh -d "hcmus.edu.vn" -o "APT.txt" -r "./data/emails"
echo "Collect email from domain finish!"
