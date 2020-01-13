#!/usr/bin/python3
"""
Function that adds 2 integers.
Return an integer: The addition of a and b
a and b must be integers or floats, otherwise raise a TypeError
exception with the messange a must be an integer or b must be an integer
"""


def add_integer(a, b=98):
    """
        a and b must be integers or floats
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
