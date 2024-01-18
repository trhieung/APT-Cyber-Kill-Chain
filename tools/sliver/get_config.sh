#!/usr/bin/expect

set path "./client_configs"
set names {"20120078" "20120083" "20120116" "20120176" "20120313"}

# Check if the folder exists, create it if not
if {![file isdirectory $path]} {
    if {[catch {file mkdir $path} error]} {
        puts "Error creating folder: $error"
        exit 1
    }
}

spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 0.1

foreach name $names {

    # Send your desired commands to the sliver-server terminal
    send "new-operator --name $name --lhost 18.143.102.216 --lport 31337 --save $path\r"
    
    # Add a delay between iterations if needed
    sleep 0.1
}

# Add a delay to make sure the new operators are created
sleep 0.1

# Close the sliver-server terminal gracefully
send "exit\r"
expect eof

# Use glob to get the list of files in the client_configs folder
set filelist [glob -nocomplain "${path}/*"]

# Copy each file individually
foreach file $filelist {
    exec cp $file "/var/www/apt_domain/configs/"
}

# Grant read and execute permissions to everyone for the copied folder and its contents
exec chmod -R +rX /var/www/apt_domain/configs/


spawn sliver-server
sleep 0.1
send "multiplayer\r"
send "operators\r"