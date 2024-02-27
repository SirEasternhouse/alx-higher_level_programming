#!/usr/bin/python3
"""Rectangle class that inherits a Base class reps a rectangle shape
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base and represents a rectangle shape.

    Attributes:
         width (int): Width of the rectangle.
         height (int): Height of the rectangle.
         x (int): X-coordinate of the rectangle's position.
         y (int): Y-coordinate of the rectangle's position.
         id (int): ID of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle's position..
            y (int,, optional): Y-coordinate of the rectangle's position.
            (int, optional): ID of the rectangle (defalt is None)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self, height):
        """Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter x atrribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """ getter y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle instance with '#' chars """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute
            
            Args:
                *args: positional arguments.
                **kwargs: Keyword argumnts.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
    
    def to_dictionary(self):
        """
        Returns the dictionary representaation of a retangle
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """ Return a string rep of rectangle instnace."""
        return"[Rectangle] ({}) {}/{}".format(
                self.id, self.x, self.__width, self.__height
                )
