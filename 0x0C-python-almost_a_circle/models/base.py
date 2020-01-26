#!/usr/bin/python3
import json


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
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
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
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