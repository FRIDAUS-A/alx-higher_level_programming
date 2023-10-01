#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the
GitHub API to display your id
"""
import sys
import requests
if __name__ == '__main__':
    url = "https://api.github.com/user"
    header = {}
    header["Authorization"] = f"Bearer {sys.argv[2]}"
    body = requests.get(url, headers=header)
    if (len(body.json()) != 2):
        print(body.json())
    else:
        print(None)
