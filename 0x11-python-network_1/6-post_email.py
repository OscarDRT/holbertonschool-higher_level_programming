#!/usr/bin/python3

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    payload = {"email": argv[2]}
    pag = requests.post(url, data=payload)
    print(pag.text)
