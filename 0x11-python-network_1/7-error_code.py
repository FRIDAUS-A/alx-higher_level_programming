#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a
request to the URL and displays the body of the response.
"""
import requests
import sys
if __name__ == '__main__':
    html = requests.get(sys.argv[1])
    if html.status_code >= 400:
        print("Error code: {}".format(html.status_code))
    else:
        print(html.text)
