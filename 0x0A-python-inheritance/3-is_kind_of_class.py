#!/usr/bin/python3
"""object is an instance of, object,inherited or specified class """


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Args:
    obj: An object to check.
    a_class: A class to compare with.

    Returns:
    bool: True if obj is an instance of a_class or its subclass,
    otherwise False.
    """
    return isinstance(obj, a_class)
