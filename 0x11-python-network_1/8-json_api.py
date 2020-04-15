#!/usr/bin/python3

import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    arg = argv[1] if len(argv) > 1 else ""
    try:
        pag = requests.post(url, data={'q': arg}).json()
        if 'id' in pag and 'name' in pag:
            print("[{}] {}".format(pag['id'], pag['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
