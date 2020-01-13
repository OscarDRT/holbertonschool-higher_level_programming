#!/usr/bin/python3
"""Function that prints My name is <first name> <last name>
first_name and last_name must be strings otherwise,
raise a TypeError exception with the message
first_name must be a string or last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
        first_name and last_name must be strings
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print('My name is', first_name, last_name)
