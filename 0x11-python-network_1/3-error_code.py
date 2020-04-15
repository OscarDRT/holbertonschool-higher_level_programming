#!/usr/bin/python3

import urllib.error
import urllib.request
from sys import argv


url = argv[1]
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("{}".format(body.decode('utf-8')))
except urllib.error.URLError as error:
    print("Error code: {}".format(error.status))
