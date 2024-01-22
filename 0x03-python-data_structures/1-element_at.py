#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:  # checking for negative index
        return None
    elif idx > len(my_list):  # checking for out of range
        return None
    else:
        return my_list[idx]
