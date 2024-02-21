#!/usr/bin/python3
"""Appends a string to the end of a text file and return the no.chars added.
"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print("Error occurred while appending to file: {}".format(e))
        return 0
