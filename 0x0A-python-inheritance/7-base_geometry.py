#!/usr/bin/python3
"""class BaseGeometry
Public instance method: def area(self)
Public instance method: def integer_validator(self, name, value)
"""


class BaseGeometry:
    def area(self):
        """
            raises an Exception with the message
            area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            value is not integer raise a TypeError
            value <= 0 raise a ValueError
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
