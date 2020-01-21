#!/usr/bin/python3
import json
def load_from_json_file(filename):
    with open(filename) as f:
        p_obj = f.read()
        return json.loads(p_obj)
