#!/usr/bin/python3
"""checking inheritance from classes"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
    obj: An object to check.
    a_class: A class to compare with.

    Returns:
    bool: True if obj is an instance of a class that inherited from a_class,
    otherwise False.
    """
    return issubclass(type(obj), a_class)
