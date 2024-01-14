#!/usr/bin/expect

set path "./client_configs"
set name "20120083"

# Check if the folder exists, create it if not
if {![file isdirectory $path]} {
    if {[catch {file mkdir $path} error]} {
        puts "Error creating folder: $error"
        exit 1
    }
}

spawn sliver-server

# Wait for sliver-server to start (you can adjust the sleep duration as needed)
sleep 1

# Send your desired commands to the sliver-server terminal
send "new-operator --name $name --lhost 18.143.102.216 --lport 31337 --save $path/${name}.cfg\r"

# Optionally, you can add more commands as needed
# send "new-operator --name $name --lhost 18.143.102.216 --lport 31337 --save $path/${name}.cfg\r"
# cp "$path/${name}.cfg" "/var/www/apt_domain/configs/"

# Add a delay to keep the sliver-server terminal window open for a while
sleep 1

# Close the sliver-server terminal gracefully
send "exit\r"
expect eof

cp "$path/${name}.cfg" "/var/www/apt_domain/configs/"

