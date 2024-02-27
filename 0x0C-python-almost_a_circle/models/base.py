#!/usr/bin/python3
"""
    Base class for managing ID attribute in other classes.
"""


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
