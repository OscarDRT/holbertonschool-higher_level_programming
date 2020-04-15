#!/usr/bin/python3

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    pag = requests.get(url)
    if (pag.status_code == 200):
        print(pag.text)
    else:
        print("Error code:", pag.status_code)
