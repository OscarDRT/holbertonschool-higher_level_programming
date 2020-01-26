#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


    def __str__(self):
        return ("[Square] (%d) %d/%d - %d"
        %(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        if len(args) != 0:
            name = ["id", "size", "x", "y"]
            i = 0
            for change in args:
                setattr(self, name[i], change)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        name = ["id", "size", "x", "y"]
        value = [self.id, self.width, self.x, self.y]
        x = {}
        i = 0
        for key in name:
            x[key] = value[i]
            i += 1
        return x