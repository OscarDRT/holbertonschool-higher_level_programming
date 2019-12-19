#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new = list(a_dictionary.keys())
        biggest = 0
        k = ""
        for key in new:
            if a_dictionary[key] > biggest:
                biggest = a_dictionary[key]
                k = key
        return k
    else:
        return None
