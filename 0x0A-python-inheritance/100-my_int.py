#!/usr/bin/python3
"""class MyInt that inherits from int
MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    def __init__(self, value):
        int.__init__(self)
        if type(value) == int:
            self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
