#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new = list(a_dictionary.keys())
        biggest = a_dictionary[new[0]]
        for key in new:
            if a_dictionary[key] > biggest:
                biggest = a_dictionary[key]
                k = key
        return k
    else:
        return None
