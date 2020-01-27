#!/usr/bin/python3
"""
This class will be the “base” of all other classes
"""


import json
import turtle


class Base:
    """
    Class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        json string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save file
        """
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                return f.write([])
            else:
                my_list = []
                for obj in list_objs:
                    my_dict = obj.to_dictionary()
                    my_list.append(my_dict)
                return f.write(cls.to_json_string(my_list))

    def from_json_string(json_string):
        """
        from json
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create
        """
        dummy = cls(1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load file
        """
        my_lis = []
        try:
            with open(cls.__name__ + ".json", "r") as f:
                contents = f.read()
                objs = cls.from_json_string(contents)
                for new in objs:
                    my_lis.append(cls.create(**new))
                return my_lis
        except IOError:
            return my_lis

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draw figure
        """
        list_objsrec = []
        for obj_rec in list_rectangles:
            dicts_rec = obj_rec.to_dictionary()
            list_objsrec.append(dicts_rec)
        for draw in list_objsrec:
            rectangle = turtle.Turtle()
            rectangle.penup()
            rectangle.setposition(draw["x"], draw["y"])
            rectangle.pendown()
            rectangle.color("red", "black")
            rectangle._delay(35)
            for leng in range(2):
                rectangle.forward(draw["width"])
                rectangle.left(90)
                rectangle.forward(draw["height"])
                rectangle.left(90)
        turtle.clearscreen()

        list_objsqure = []
        for obj_square in list_squares:
            dicts_rec = obj_square.to_dictionary()
            list_objsqure.append(dicts_rec)
        for draw2 in list_objsqure:
            square = turtle.Turtle()
            square.penup()
            square.setposition(draw2["x"], draw2["y"])
            square.pendown()
            square.color("red", "black")
            square._delay(35)
            for leng in range(4):
                square.forward(draw2["size"])
                square.left(90)
        turtle.exitonclick()
