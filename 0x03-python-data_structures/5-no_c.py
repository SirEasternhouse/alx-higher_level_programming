#!/usr/bin/python3
def no_c(my_string):
    c_rmv = ''

    for char in my_string:
        if char.lower() != 'c':
            c_rmv += char
    return c_rmv
