#!/bin/bash

# apache2 give download permissions

# Specify the paths to the directories
DIRECTORIES=(
    "/var/www/apt_domain"
    "/var/www/apt_domain/sessions"
    "/var/www/apt_domain/beacons"
    "/var/www/apt_domain/configs"
)

# Loop through the directories and change ownership
for dir in "${DIRECTORIES[@]}"; do
    sudo chown www-data:www-data "$dir"
done
