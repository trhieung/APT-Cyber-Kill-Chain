# Gophish - CyberKill Train Delivery Tool

## Introduction
Gophish is a tool used for conducting phishing campaigns and simulating phishing attacks. It provides a platform to design and execute phishing emails and landing pages to assess the security awareness of an organization.

## Installation
To install Sliver, refer to the official Kali Linux tools page: [Kali Tools](https://www.kali.org/tools/). Detailed installation instructions can be found [here](https://www.kali.org/tools/gophish/).

## Usage
This folder contains a Python script that facilitates interactions with a Gophish service running locally. If you're using a remote server, SSH connection with port forwarding is required (see Accessing the Service).

The script, written in custom_gophish.py, automates interactions with Gophish. It retrieves emails from the default link loaded from the .env file and obtains payload/text/other content from the specified path in that .env, sending them to emails.

To run the script:
```
python run_custom.py
```
or
```
python3 run_custom.py
```

## Local config
It's advisable to change the port of the Gophish server to avoid conflicts with other services. In this project, it conflicts with the Apache2 service.

## Accessing the Service
To access the gophish-server from your local machine and forward port 3333, use the following SSH command:

```bash
ssh -i <path_to_pem_file> -L <your_localport>:127.0.0.1:3333 <name>@<public_ip>
```
## Default Credentials

- **Username:** admin
- **Password:** 123456789
