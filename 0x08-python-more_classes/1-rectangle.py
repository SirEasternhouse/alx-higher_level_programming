#!/usr/bin/python3
class Rectangle:
    """Represents a rectangle with a width and height."""

    
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object.
            Args:
                width (int, optional): The width of the rectangle.
                height (int, optional): The height of the rectangle.
        """
        self._validate_width(width)
        self._validate_height(height)
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        self._validate_height(value)
        self.__height = value

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        self._validate_width(value)
        self.__width = value

    def _validate_height(self, value):
        """Validates the height value."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    def _validate_width(self, value):
        """Validates the height value."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "{{'_Rectangle__width': {}, '_Rectangle__height': {}}}".format(
                self.__width, self.__height)
