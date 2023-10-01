#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the
URL and displays the value of the variable X-Request-Id in
the response header
"""
import requests
import sys
if __name__ == '__main__':
    html = requests.get(sys.argv[1])
    if 'X-Request-Id' in html.headers:
        print(html.headers.get("X-Request-Id"))
