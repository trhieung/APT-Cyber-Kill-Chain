# Sliver - Penetration Testing Tool

## Introduction
Sliver is a powerful penetration testing tool included in the Kali Linux distribution. It enables various operations within the Cyber Kill Chain, particularly in the stages of Weaponization and Command & Control. This tool allows for the creation and execution of payloads in different formats to establish covert communication channels with compromised systems.

## Installation
To install Sliver, refer to the official Kali Linux tools page: [Kali Tools](https://www.kali.org/tools/). Detailed installation instructions can be found [here](https://www.kali.org/tools/sliver/).

Alternatively, you can clone the Sliver repository [from GitHub](https://github.com/BishopFox/sliver) for testing.
Once cloned, execute the following command to install Sliver:

```git clone https://github.com/BishopFox/sliver```


## Usage
This folder contains shell scripts that facilitate interactions with the Sliver server. Most of these scripts are written using the Expect scripting language to automate interactions with the Sliver server in a consistent terminal environment.

## Supported Payload Formats
Sliver supports the creation of payloads in two main formats:
- Executable (.exe) files, which are typically under 10KB in size.
- PowerShell script files (.ps1), which are approximately 100KB in size.

These payloads are generated from a stager code, known as "quiet light," which is usually under 10KB in size.

## Multi-Mode Support
Sliver supports running in multiple modes, with the default mode listening on port 31137 of the server.

For more information on how to utilize Sliver effectively, please refer to the official documentation and resources provided by the developers.