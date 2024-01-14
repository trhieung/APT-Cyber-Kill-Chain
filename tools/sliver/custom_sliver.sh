#!/bin/bash

path="../client_configs/"
name="20120083"

sliver-server
new-operator --name "$name" --lhost 18.143.102.216 --lport 31337 --save "${name}_client_18.143.102.216_31337"
exit

copy "${name}_client_18.143.102.216_31337" "/var/www/apt_domain/configs/"