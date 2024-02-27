#!/usr/bin/python3
"""
    Square class inherits from Rectangle and reps a square shape.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class representing a square shape.
        Attributes:
            size (int): Size of the square.
            x (int): X-coordinate of the square's position.
            y (int): Y-coordinate of the square's position.
            id (int): ID of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): Size of the square.
            x (int, opt): X-coordinate of square's position (defualt is 0).
            y (int, opt): Y-coordinate of square's position (defualt is 0).
            id (int, opt): ID of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """
        Assigns attributes to square.

        Args:
            *args: Positional arguments (id, size, x, y).
            **kwargs: Keyword arguments (attribute=value).

        Note:
            if *args exist and is not empty, **kwargs is skipped
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
