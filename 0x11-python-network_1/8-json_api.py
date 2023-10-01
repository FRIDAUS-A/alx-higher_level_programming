#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""
import sys
import requests

if __name__ == '__main__':
    data = {}
    if len(sys.argv) == 1:
        data['q'] = ""
    else:
        data['q'] = sys.argv[1]
    html = requests.post("http://0.0.0.0:5000/search_user", data=data)
    json = html.json()
    try:
        if json == {}:
            print("No result")
        else:
            print(f"[{json['id']}]  {json['name']}")
    except ValueError:
        print("Not a valid JSON")
