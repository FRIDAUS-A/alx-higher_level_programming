#!/bin/bash
#a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body.
curl -s -X POST @"$2" "$1"
