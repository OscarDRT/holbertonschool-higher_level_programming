#!/usr/bin/python3
import json, sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
new_list = []
filename = "add_item.json"
for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])
save_to_json_file(new_list, filename)
load_from_json_file(filename)
