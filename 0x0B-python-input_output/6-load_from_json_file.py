#!/usr/bin/python3
""" Creates an object from a JSON file. """


import json


def load_from_json_file(filename):
    """
        Args:
        filename (str): The name of the JSON file to load the object from.

        Returns:
            object: The Python object created from the JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)
