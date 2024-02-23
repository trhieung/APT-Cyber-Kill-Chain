# SpiderFoot

## Introduction

SpiderFoot is a reconnaissance tool that gathers information about a target by utilizing various data sources on the internet. It can be particularly useful for gathering email addresses associated with a domain.

## Installation

To install SpiderFoot, refer to the official Kali Linux tools page: [Kali Tools](https://www.kali.org/tools/). Detailed installation instructions can be found [here](https://www.kali.org/tools/spiderfoot/).

## Usage

SpiderFoot can be used to retrieve email addresses associated with a domain. It requires three arguments:
- `d`: Domain name
- `o`: Output file name
- `r`: Route/path/directory to save the output file

To explore the available modules and filter them based on functionality, execute the following commands (found within the emails_from_domain.sh file):
```
spiderfoot -M | grep -E 'email|web'
```
Furthermore, to identify the types of information currently being utilized, execute:
```
spiderfoot -T | grep -E 'EMAIL|WEB'```
```
Here's an example of how to retrieve emails from a domain:
```
emails_from_domain.sh -d "danck12.github.io" -o "APT.txt" -r "./data/emails"
```

## Troubleshooting: Running the .sh File

Check your permissions file.
```
ls -l ./emails_from_domain.sh
```

Make executiono enable if needed 
```
chmod +x ./emails_from_domain.sh
```