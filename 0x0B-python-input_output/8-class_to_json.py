#!/usr/bin/python3
""" Convert instance of a class to a dict des suitable for JSON serial."""


def class_to_json(obj):
    """

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary rep of the object with serializable attributes.

    Raises:
        TypeError: If the input object is not an instance of a class.
    """
    if not isinstance(obj, type):
        raise TypeError("Input must be an instance of a class.")

    attributes = vars(obj)

    serializable_dict = {}

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[attr] = value

    return serializable_dic
