#!/usr/bin/expect
spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 1

# Send your desired commands to the sliver-server terminal
send "multiplayer\r"

# Add a delay to keep the sliver-server terminal window open for a while
sleep 1
