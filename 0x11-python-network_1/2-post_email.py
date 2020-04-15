#!/usr/bin/python3

import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        the_page = the_page.decode('utf-8')
        print(the_page)
