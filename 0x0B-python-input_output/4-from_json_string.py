#!/usr/bin/python3
""" Returns a Python object represented by a JSON string."""


import json


def from_json_string(my_str):
    """
        Args:
        my_str (str): The JSON string representing the object.

        Returns:
            object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
