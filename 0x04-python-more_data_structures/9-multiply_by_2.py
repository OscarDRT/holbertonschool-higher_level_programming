#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict.copy(a_dictionary)
    for i in a_dictionary:
        new[i] = new[i] * 2
    return new
