#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_dict = {}

    for key in a_dictionary:
        multiplied_dict[key] = a_dictionary[key] * 2
    return multiplied_dict
