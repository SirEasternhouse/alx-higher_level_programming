#!/usr/bin/python3
"""A class representing an integer with inverted equality operators """


class MyInt(int):
    """
    A class representing an integer with inverted equality operators.

    Inherits:
    int: A built-in integer type.

    Public Methods:
    __eq__(other): Overrides the equality operator (==).
    __ne__(other): Overrides the inequality operator (!=).
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to return the opposite result.

        Args:
        other: The object to compare with.

        Returns:
        bool: True if self is not equal to other, otherwise False.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to return the opposite result.

        Args:
        other: The object to compare with.

        Returns:
        bool: True if self is equal to other, otherwise False.
        """
        return super().__eq__(other)
