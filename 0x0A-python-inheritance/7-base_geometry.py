#!/usr/bin/python3
"""Base class for geometry operations."""


class BaseGeometry:
    """
        A base class for geometry operations.

        Public Methods:
        area(): Raises an Exception with the message "area() is not implemented".
        integer_validator(name, value): Validates an integer value.
    """

    def area(self):
        """
        Raises an Exception indicating that the method is not implemented.

        Raises:
        Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
