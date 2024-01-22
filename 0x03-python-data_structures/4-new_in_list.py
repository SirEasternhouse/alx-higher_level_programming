#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = list.copy(my_list)  # creating a copy of orgiginal list

    if idx < 0 or idx > len(copy_list):  # out of range and negative idx
        return copy_list
    else:
        copy_list[idx] = element  # modified copy
        return copy_list
