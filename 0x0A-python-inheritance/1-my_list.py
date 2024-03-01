#!/usr/bin/python3
"""Class list that inheritts from my list"""


class MyList(list):
    """my list that inherits from list function"""
    def print_sorted(self):
        """printing a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
