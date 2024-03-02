#!/usr/bin/python3
"""Rectangle class inhering base geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Inherits:
    BaseGeometry: A base class for geometry operations.

    Public Methods:
    __init__(width, height): Initializes the Rectangle with width and height.
    __str__(): Returns the string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
        str: The string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
