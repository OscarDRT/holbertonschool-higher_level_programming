#!/usr/bin/python3


def find_peak(list_of_integers):
    if list_of_integers:
        max = list_of_integers[0]
        for num in list_of_integers:
            if num >= max:
                max = num
        return max
    return None
