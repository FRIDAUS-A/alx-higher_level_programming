#!/usr/bin/python3
"""
Holberton Interview Question
"""
import sys
import requests

if __name__ == '__main__':
    url = "https://api.github.com/repos/" + sys.argv[2] + "/" +\
                                            sys.argv[1] + "/commits"
    body = requests.get(url)
    json = body.json()
    count = 0
    for mem in json:
        count += 1
        print(f"{mem.get('sha')}:"
              f"{mem.get('commit').get('author').get('name')}")
        if count == 10:
            break
