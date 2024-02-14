#!/usr/bin/python3
""" this class can be used to create a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """ 
        Initializes a new Rectangle object.

        Args:
            width (int,optional): The width of the rectangle. Default to 0.
            height (int,optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than 0.
        """
        self._validate_dimension(width, "width")
        self._validate_dimension(height, "height")
        self._width = width
        self._height = height

    @property
    def width(self):
        """ 
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        self._validate_dimension(value, "width")
        self._width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        self._validate_dimension(value, "height")
        self._height = value

    def _validate_dimension(self, value, dimension_name):
        """
        Validates a dimension value.

        Args:
            value: The value to validate.
            dimension_name: The name of the dimension (e.g., "width" or "height").

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(dimension_name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(dimension_name))
