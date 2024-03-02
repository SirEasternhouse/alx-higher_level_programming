#!/usr/bin/python3
"""Square class inheriting from Rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Inherits:
    Rectangle: A class representing a rectangle.

    Public Methods:
    __init__(size): Initializes the Square with size.
    """

    def __init__(self, size):
        """
        Initialize the Square with size.

        Args:
        size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
        str: The string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
