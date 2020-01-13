#!/usr/bin/python3
"""Function that prints a square with the character #
size is the size length of the square
size must be an integer, otherwise
raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception
with the message size must be >= 0
f size is a float and is less than 0,
raise a TypeError exception with the message size must be an integer
"""


def print_square(size):
    """
        size is the size length of the square, size must be integer
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        if size == 0:
            size = size
        else:
            for i in range(0, size):
                print("#" * size)
