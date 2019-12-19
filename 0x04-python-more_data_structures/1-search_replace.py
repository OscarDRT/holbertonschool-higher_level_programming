#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        return list(map(lambda i: replace if i == search else i,my_list))
