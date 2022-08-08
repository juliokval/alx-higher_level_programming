#!/usr/bin/python3
"""The Base Class"""


import json
import os


class Base:
    """The Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class initialization"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == {}:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        content = []
        if list_objs is not None:
            for item in list_objs:
                content.append(item.to_dictionary())
        with open(filename, 'w', encoding="utf-8") as f:
            return f.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary != {}:
            if cls.__name__ == 'Rectangle':
                new_instance = cls(1, 1)
            if cls.__name__ == 'Square':
                new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
            formattedContent = (cls.from_json_string(content))
            return [cls.create(**item) for item in formattedContent]
