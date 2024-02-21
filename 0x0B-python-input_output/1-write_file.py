#!/usr/bin/python3
"""Writes a string to a text file and returns the number of chars written."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of chars written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.

    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print("Error occurred while writing to file: {}".format(e))
        return 0
