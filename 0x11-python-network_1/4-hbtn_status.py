#!/usr/bin/python3

import requests


if __name__ == "__main__":
    pag = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(pag.text)))
    print("\t- content: {}".format(pag.text))
