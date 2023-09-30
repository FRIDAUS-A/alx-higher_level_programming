#!/bin/bash
#a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body.
curl -s -X POST -d "@$2" "$1"
