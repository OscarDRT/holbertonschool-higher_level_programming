#!/usr/bin/python3

import requests


if __name__ == "__main__":
    pag = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("    - type: {}".format(type(pag.text)))
    print("    - content: {}".format(pag.text))
