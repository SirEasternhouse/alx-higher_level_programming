#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = list(reversed(my_list))

    for i in reversed_list:
        print("{}".format(i, end=''))