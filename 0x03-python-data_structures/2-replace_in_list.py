#!/bin/usr/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:  # negative idx to return original list
        return my_list
    elif idx > len(my_list):  # idx out of range return original list
        return my_list
    else:  # modified list with new element
        my_list[idx] = element
        return my_list
