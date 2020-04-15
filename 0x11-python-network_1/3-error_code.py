#!/usr/bin/python3

import urllib.request
from sys import argv


if __name__ == '__main__':
    try:
        url = argv[1]
        with urllib.request.urlopen(url) as pag:
            if pag.status == 200:
                print(pag.read().decode('utf-8'))
            else:
                print("Error code: {}".format(pag.status))
    except Exception as e:
        print("Error code: {}".format(e.code))
