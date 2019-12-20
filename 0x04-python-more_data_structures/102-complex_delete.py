#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = list(a_dictionary.keys())
    for i in range(len(a_dictionary)):
        if value == a_dictionary[a[i]]:
            del a_dictionary[a[i]]
    return a_dictionary
