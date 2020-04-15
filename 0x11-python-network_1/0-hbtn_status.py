#!/usr/bin/python3
import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        body = response.read()
    print("Body response:")
    print("    - type: {}".format(type(body)))
    print("    - content: {}".format(body))
    print("    - utf8 content: {}".format(body.decode('utf-8')))
