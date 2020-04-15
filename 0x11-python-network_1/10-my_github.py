#!/usr/bin/python3

import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    passworld = argv[2]
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(user, passworld)).json()
        print(response['id'])
    except:
        print("None")
