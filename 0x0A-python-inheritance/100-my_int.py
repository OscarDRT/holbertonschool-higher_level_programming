#!/usr/bin/python3
class MyInt(int):
    def __init__(self, value):
        int.__init__(self)
        if type(value) == int:
            self.value = value

        