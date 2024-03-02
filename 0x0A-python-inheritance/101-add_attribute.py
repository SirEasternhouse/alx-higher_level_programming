#!/usr/bin/python3
"""Adds a new attribute to an object if it's possible """


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception if the object can't have new attributes.

    Args:
    obj: The object to which the attribute will be added.
    name (str): The name of the attribute.
    value: The value of the attribute.

    Raises:
    TypeError: If the object can't have new attributes.
    """
    if (
            hasattr(obj, "__dict__") or
            hasattr(obj, "__slots__") or
            isinstance(obj, dict)
            ):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
