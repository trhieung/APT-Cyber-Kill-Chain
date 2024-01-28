#!/usr/bin/expect

# Prepare stager.c file
exec ./tools/sliver/get_stagers.sh

# create .exe file from another .sh file
exec ./tools/sliver/exe_from_c.sh

# Ativate Sliver server
spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 0.1

# Continue using sliver-server
send "multiplayer\r"
send "operators\r"
send "jobs\r"
send "profiles\r"