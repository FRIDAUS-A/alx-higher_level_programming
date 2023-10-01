#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys
if __name__ == '__main__':
    dict = {}
    dict['email'] = sys.argv[2]
    value = urllib.parse.urlencode(dict)
    value = value.encode('ascii')
    req = urllib.request.Request(sys.argv[1], value)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    print(htm1)
