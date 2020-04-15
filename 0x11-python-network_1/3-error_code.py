#!/usr/bin/python3

import urllib.request
from sys import argv


url = argv[1]
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        if response.status == 200:
            print(response.read().decode('utf-8'))
        else:
            print("Error code: {}".format(response.status))
except urllib.error.URLError as error:
    print("Error code: {}".format(error.code))
