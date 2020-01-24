#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.vali_wihe(width=width, height=height)
        self.vali_xy(x=x, y=y)
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.vali_wihe(width=value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.vali_wihe(height=value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.vali_xy(x=value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.vali_xy(y=value)
        self.__y = value

    def vali_wihe(self, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.items():
                if type(value) is not int:
                    raise TypeError("%s must be an integer" %(key))
                elif value <= 0:
                    raise ValueError("%s must be > 0" %(key))

    def vali_xy(self, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.items():
                if type(value) is not int:
                    raise TypeError("%s must be an integer" %(key))
                elif value < 0:
                    raise ValueError("%s must be >= 0" %(key))

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        x = ((" " * self.__x) + ("#" * self.__width) + "\n") * (self.__height - 1)
        y = (" " * self.__x) + ("#" * self.__width)
        z = "\n" * self.__y
        print(z + x + y)

    def __str__(self):
        return ("[Rectangle] (%d) %d/%d - %d/%d"
        %(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        if len(args) != 0:
            name = ["id", "width", "height", "x", "y"]
            i = 0
            for change in args:
                setattr(self, name[i], change)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
