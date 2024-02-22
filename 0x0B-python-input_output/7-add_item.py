#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file """


import sys
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to write the JSON rep to.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)


arguments = sys.argv[1:]

try:
    existing_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_items = []

existing_items.extend(arguments)

save_to_json_file(existing_items, "add_item.json")
