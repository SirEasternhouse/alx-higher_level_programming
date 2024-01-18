#!/usr/bin/python3


import sys


def add_arguments(*args):
    return sum(map(int, args))


if __name__ == "__main__":
    arguments = sys.argv[1:]

    if arguments:
        result = add_arguments(*arguments)
        print(result)
    else:
        print("No arguments provided")
