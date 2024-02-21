#!/usr/bin/python3
""" Create a JSON representaion of an object string"""


import json


def to_json_string(my_obj):
    """
        Args:
        my_obj: The object to be serialized to JSON.

        Returns:
            str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
