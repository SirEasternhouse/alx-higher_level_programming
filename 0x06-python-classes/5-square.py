#!/usr/bin/python3
"""This class can be used to create square objects"""


class Square:
    """defining a class square with a size attirbute"""

    def __init__(self, size=0):
        """ parameters:
            param 1: size
                the size of the square starting at 0
        """
        self.__size = size

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

    def area(self):
        """ Returns the area of a square """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with char # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
