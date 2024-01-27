#!/bin/bash

# Default values
DOMAIN="hcmus.edu.vn"
OUTPUT_FILE="emails_hcmus_edu_vn.txt"
OUTPUT_DIR="."

# Parse command line arguments
while getopts ":d:o:r:" opt; do
  case $opt in
    d)
      DOMAIN="$OPTARG"
      ;;
    o)
      OUTPUT_FILE="$OPTARG"
      ;;
    r)
      OUTPUT_DIR="$OPTARG"
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

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Your existing script
COMMAND="spiderfoot \
          -m \$(spiderfoot -M | grep -E 'email|web' | awk '{print \$1}' | tr '\\n' ',' | sed 's/,\$//')\$ \
          -t \$(spiderfoot -T | grep -E 'EMAIL|WEB' | awk '{print \$1}' | tr '\\n' ',' | sed 's/,\$//')\$ \
          -f -s $DOMAIN > $OUTPUT_DIR/raw_output.txt\

        awk \
          -F'\t' '{print \$3}' $OUTPUT_DIR/raw_output.txt | grep -E '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b' > $OUTPUT_DIR/$OUTPUT_FILE\

        rm $OUTPUT_DIR/raw_output.txt"
# echo $COMMAND

# Execute the command
eval "$COMMAND"
