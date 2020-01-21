#!/usr/bin/python3
import json

def from_json_string(my_str):
    decoded = json.loads(my_str)
    return decoded