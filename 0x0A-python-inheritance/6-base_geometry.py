#!/usr/bin/python3
""" Base class for geometry operations."""


class BaseGeometry:
    """
    A base class for geometry operations.

    Public Methods:
    area(): Raises an Exception with the message "area() is not implemented".
    """

    def area(self):
        """
        Raises an Exception indicating that the method is not implemented.

        Raises:
        Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")
