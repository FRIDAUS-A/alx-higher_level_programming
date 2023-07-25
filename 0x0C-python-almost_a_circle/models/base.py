#!/usr/bin/python3
"""THE BASE CLASS"""


import json


class Base:
    """Base class for other classes"""
    __nb_objects = 0
    def __init__(self, id=None):

        """constructor
            Args:
                id (int): id for the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        json_string = json.dumps(list_dictionaries)
        return (json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return ([])
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if (cls.__name__ == "Rectangle"):
            dummy = cls(2, 2)
        elif (cls.__name__ == "Square"):
            dummy = cls(2)
        else:
            dummy = None
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(fileaname, "r") as file:
                json_tmp = file.read()
                result_list = cls.from_json_string(json_tmp)
                if result_list == []
                return []
                instances = [cls.create(**d) for d in result_list]
                return (instances)
        except FileNotFoundError:
            return []
