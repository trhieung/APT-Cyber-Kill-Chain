#!/bin/bash
# Spiderfoot Email Extraction Script

# Default values
default_domain="hcmus.edu.vn"
default_output_file="email.txt"

# Function to confirm with the user
confirm_default_values() {
  read -r -p "Using default values: Domain=$default_domain, Output File=$default_output_file. Do you want to continue? (y/n): " response
  case "$response" in
    [yY])
      ;;
    *)
      echo "Script execution aborted."
      exit 0
      ;;
  esac
}

while getopts ":s:o:" opt; do
  case $opt in
    s)
      domain="$OPTARG"
      ;;
    o)
      output_file="$OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# Check if domain and output_file are not provided
if [ -z "$domain" ]; then
  domain="$default_domain"
  confirm_default_values
fi

if [ -z "$output_file" ]; then
  output_file="$default_output_file"
  confirm_default_values
fi

# Run Spiderfoot to gather email addresses from modules and transforms
email_addresses=$(spiderfoot -M | grep email | awk '{print $1}' | tr '\n' ',' | sed 's/,$//')
target_emails=$(spiderfoot -T | grep EMAIL | awk '{print $1}' | tr '\n' ',' | sed 's/,$//')

# Run Spiderfoot with the collected email addresses and target emails
spiderfoot -m "$email_addresses" -t "$target_emails" -f -s "$domain" > raw_output.txt

# Extract and filter email addresses from the raw output
grep -E -o '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}' raw_output.txt > "$output_file"

# Clean up: Remove the raw output file
rm raw_output.txt

echo "Email extraction completed. Results saved to $output_file."
