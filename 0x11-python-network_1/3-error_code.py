#!/usr/bin/python3

import urllib.error
import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print("{}".format(body.decode('utf-8')))
    except urllib.error.URLError as error:
        print(error.status)
