#!/usr/bin/python3
"""This class can be used to create square objects"""


class Square:
    """defining a class square with size and position attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """ parameters:
           param 1: size
               the size of the square starting at 0
           param 2: position
               a tuple of 2 integers representing the position of the square
       """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieving the attribute value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """value: checking the integer validity of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """retrieving the attribute value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """value: checking the validity of position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns the area of a square """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with the character #,
        taking position into account """
        if self.__size == 0:
            print()
        else:
            x_offset = " " * self.__position[0]
            y_offset = "\n" * (self.__position[1] - 1)
            print(y_offset, end="")
            for i in range(self.__size):
                print(x_offset + "#" * self.__size)
