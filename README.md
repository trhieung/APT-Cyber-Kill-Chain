# APT-Cyber-Kill-Chain

## Server Access

To access the server, use SSH with the provided key file:

```bash
ssh -i <path_to_pem_file> <name>@<public_ip>
```

## Tools

The toolkit includes the following tools:

### SpiderFoot
During the cyberkill training, this tool is considered for the reconnaissance phase

- [SpiderFoot on Kali Tools](https://www.kali.org/tools/spiderfoot/)
- [SpiderFoot on GitHub](https://github.com/smicallef/spiderfoot)

more detail (here)[https://github.com/trhieung/APT-Cyber-Kill-Chain/tree/main/tools/spiderfoot]

### GoPhish
During the cyberkill training, this tool is considered for the Delivery phase

- [GoPhish on Kali Tools](https://www.kali.org/tools/gophish)
- [GoPhish on GitHub](https://github.com/gophish/gophish)

more detail (here)[https://github.com/trhieung/APT-Cyber-Kill-Chain/tree/main/tools/gophish]

### Metasploit-Framework
During the cyberkill training, this tool is considered for the exploitation and installation phases. Our objective is to locate the relevant components within this framework and the Sliver C2 framework. This involves installing the payload and subsequently reconnecting to the Sliver terminal rather than using the mfsconsole within the current framework.

- [Metasploit on Kali Tools](https://www.kali.org/tools/metasploit-framework/)
- [Metasploit on GitHub](https://github.com/rapid7/metasploit-framework)

### Sliver
During the cyberkill training, this tool is considered for weaponization and command&control phases

- [Sliver on Kali Tools](https://www.kali.org/tools/sliver/)
- [Sliver on GitHub](https://github.com/BishopFox/sliver)

more detail (here)[https://github.com/trhieung/APT-Cyber-Kill-Chain/tree/main/tools/sliver/]

## Documentation
Work in progress