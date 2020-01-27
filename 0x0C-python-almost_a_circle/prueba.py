#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    dict1 = r1.to_dictionary()
    r2 = Square(8, 2, 4, 6)
    dict2 = r2.to_dictionary()
    json_dictionary = Base.to_json_string([dict1, dict2])
    print(dict1)
    print(dict2)
    print(type(dict1))
    print(type(dict2))
    print(json_dictionary)
    print(type(json_dictionary))