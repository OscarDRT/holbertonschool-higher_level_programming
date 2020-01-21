#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""class Rectangle that inherits from BaseGeometry
area() method
str() should return, the following
rectangle description: [Rectangle] <width>/<height>
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """
            return area of rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
            return [Rectangle] <width>/<height>
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
