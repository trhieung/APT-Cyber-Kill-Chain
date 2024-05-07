# APT-Cyber-Kill-Chain

## Server Access

To access the server, use SSH with the provided key file:

```bash
ssh -i <path_to_pem_file> <name>@<public_ip>
```

## Requirements
### Installation
Ensure you have the following packages installed:
```
sudo apt install apache2
sudo apt install spiderfoot
sudo apt install gophish
sudo apt install metasploit-framework
sudo apt install sliver
```

Install Python libraries using pip:
```
pip install gophish
pip install python-dotenv
pip install pexpect
```

### Configuration
* **Apache2 Setting**: A public website showcasing the server's folder structure is being constructed, running on the Apache2 service. You can access it here. Note that this setup is solely for demonstration purposes and lacks firewall security measures.

* **Sliver Setting**: Port 8080 is designated on the server for listening, facilitating mtls binding with a stager on the server.

* **Gophish Setting**: To streamline the configuration between the Gophish server and mtls port initiated on the sliver-server, we recommend modifying the Gophish server port in the default setting file located at */etc/gophish/config.json*. Go to the specified path and modify the port to your desired value.
## Tools

The toolkit includes the following tools:

### SpiderFoot
During the cyberkill training, this tool is considered for the reconnaissance phase

- [SpiderFoot on Kali Tools](https://www.kali.org/tools/spiderfoot/)
- [SpiderFoot on GitHub](https://github.com/smicallef/spiderfoot)

more detail [here](https://github.com/trhieung/APT-Cyber-Kill-Chain/tree/main/tools/spiderfoot)

### GoPhish
During the cyberkill training, this tool is considered for the Delivery phase

- [GoPhish on Kali Tools](https://www.kali.org/tools/gophish)
- [GoPhish on GitHub](https://github.com/gophish/gophish)

more detail [here](https://github.com/trhieung/APT-Cyber-Kill-Chain/tree/main/tools/gophish)

### Metasploit-Framework
During the cyberkill training, this tool is considered for the exploitation and installation phases. Our objective is to locate the relevant components within this framework and the Sliver C2 framework. This involves installing the payload and subsequently reconnecting to the Sliver terminal rather than using the mfsconsole within the current framework.

- [Metasploit on Kali Tools](https://www.kali.org/tools/metasploit-framework/)
- [Metasploit on GitHub](https://github.com/rapid7/metasploit-framework)

### Sliver
During the cyberkill training, this tool is considered for weaponization and command&control phases

- [Sliver on Kali Tools](https://www.kali.org/tools/sliver/)
- [Sliver on GitHub](https://github.com/BishopFox/sliver)

more detail [here](https://github.com/trhieung/APT-Cyber-Kill-Chain/tree/main/tools/sliver/)

## Documentation
This documentation pertains to the project developed as part of the graduation thesis at Ho Chi Minh University of Science, specifically within the Department of Information Technology, specializing in Information Security.

The complete documentation, detailing the entire process from inception to completion, has been prepared for internal review, including the involvement of team members and the guidance provided by the project supervisor. For privacy reasons, the full documentation cannot be publicly disclosed.

For inquiries or further information, please contact 20120083@student.hcmus.edu.vn. In case of any issues with the student email, an alternative contact can be made via nthieu.ngtr@gmail.com
