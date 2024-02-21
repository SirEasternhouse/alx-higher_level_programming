#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Default is an empty string.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file is not found.
    """
    try:
        with open(filename, "r", encoding="utg-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("File '{}' not found.".format(filename))
