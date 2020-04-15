#!/usr/bin/python3

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        pag = requests.get(url)
        print(pag.headers["X-Request-Id"])
    except:
        pass
