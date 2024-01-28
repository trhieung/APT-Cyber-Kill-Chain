#!/usr/bin/expect

set payload_c "./data/payloads/win_stager.c"
set path "./data/payloads"

# Prepare stager.c file
puts "Waiting for default stager.c created"
exec ./tools/sliver/get_stagers.sh $payload_c
puts "Default stager.c create successfully saving at $path!"

# Create .exe file from another .sh file
puts "Waiting for converting stager.c to stager.exe"
exec ./tools/sliver/exe_from_c.sh
puts "Default stager.exe create successfully saving at $path!"

# # Ativate Sliver server
# spawn sliver-server

# # Wait for sliver-server to start (you can adjust the sleep duration as needed)
# sleep 0.1

# # Continue using sliver-server
# send "multiplayer\r"
# send "operators\r"
# send "jobs\r"
# send "profiles\r"