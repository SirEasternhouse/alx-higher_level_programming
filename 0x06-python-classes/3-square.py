#!/usr/bin/python3
"""This class can be used to create square objects"""


class Square:
    """defining a class square with a size attirbute"""
    def __init__(self, size=0):
        """ parameters:
            param 1: size
                        the size of the square starting at 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size mus be >= 0")
        else:
            self.__size = size

    """calculating the area of the square"""
    def area(self):
        """ Returns the area of a square """
        return self.__size ** 2
