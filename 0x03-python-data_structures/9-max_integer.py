#!/usr/bin/python3
def max_integer(my_list=[]):
    sorted_list = sorted(my_list, key=None, reverse=True)
    return sorted_list[0] if sorted_list else None
