#!/usr/bin/python3
""" Check if the object is exactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
    obj: An object to check.
    a_class: A class to compare with.

    Returns:
    bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
