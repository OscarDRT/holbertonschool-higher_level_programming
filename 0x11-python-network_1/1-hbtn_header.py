#!/usr/bin/python3

from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        headers = response.info()

    print(headers["X-Request-Id"])
