#!/usr/bin/python3

import urllib.error
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        url = argv[1]
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("{}".format(body.decode('utf-8')))
    except urllib.error.URLError as error:
        print(error.status)
