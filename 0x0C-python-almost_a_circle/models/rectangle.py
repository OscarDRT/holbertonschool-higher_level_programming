#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """comment"""
        self.vali_wihe(width=width, height=height)
        self.vali_xy(x=x, y=y)
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """comment"""
        return self.__width

    @width.setter
    def width(self, value):
        """comment"""
        self.vali_wihe(width=value)
        self.__width = value

    @property
    def height(self):
        """comment"""
        return self.__height

    @height.setter
    def height(self, value):
        """comment"""
        self.vali_wihe(height=value)
        self.__height = value

    @property
    def x(self):
        """comment"""
        return self.__x

    @x.setter
    def x(self, value):
        """comment"""
        self.vali_xy(x=value)
        self.__x = value

    @property
    def y(self):
        """comment"""
        return self.__y

    @y.setter
    def y(self, value):
        """comment"""
        self.vali_xy(y=value)
        self.__y = value

    def vali_wihe(self, **kwargs):
        """comment"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if type(value) is not int:
                    raise TypeError("%s must be an integer" % (key))
                elif value <= 0:
                    raise ValueError("%s must be > 0" % (key))

    def vali_xy(self, **kwargs):
        """comment"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if type(value) is not int:
                    raise TypeError("%s must be an integer" % (key))
                elif value < 0:
                    raise ValueError("%s must be >= 0" % (key))

    def area(self):
        """comment"""
        return (self.__width * self.__height)

    def display(self):
        """comment"""
        w = (self.__height - 1)
        x = ((" " * self.__x) + ("#" * self.__width) + "\n") * w
        y = (" " * self.__x) + ("#" * self.__width)
        z = "\n" * self.__y
        print(z + x + y)

    def __str__(self):
        """comment"""
        m = "[Rectangle] ({}) {}/{} - {}/{}"
        return m.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """comment"""
        if len(args) != 0:
            name = ["id", "width", "height", "x", "y"]
            i = 0
            for change in args:
                setattr(self, name[i], change)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """comment"""
        name = ["id", "width", "height", "x", "y"]
        value = [self.id, self.__width, self.__height, self.__x, self.__y]
        x = {}
        i = 0
        for key in name:
            x[key] = value[i]
            i += 1
        return x
