#!/usr/bin/python3
"""
    Base class for managing ID attribute in other classes.
"""
import json


class Base:
    """
    Base class for managing id attributes in other classes.
    Attributes:
        __nb_objects (int): Private class attribute to keep track of no. obj.
        id (int): Public instance attribute representing the obj ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base Object

            Args:
                id(int,optional): ID of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert a list of dictionaries to JSON string.

        Args:
            list_dictionaries (list): list of dictiionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write the JSON string representatin of list_objs to a file.

        Args:
            list_objs (list): lists of instances inheriting from Base
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    )
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string representing a list of dictionaries

        Returns:
            list: List of dictionaries represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes set using a dictionary.

        Args:
            **dictionary: Dictionary containing attributes to set.

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise TypeError("Unsupported class type")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a JSON file.

        Returns:
            list: list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dict_list = cls.from_json_string(json_data)
                return [cls.create(**dictionary) for dictionary in dict_list]
        except FileNotFoundError:
            return []
