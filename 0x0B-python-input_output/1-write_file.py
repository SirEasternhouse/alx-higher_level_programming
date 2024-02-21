#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. Default is an empty string.
        text (str): The string to write to the file. Default is an empty string.

    Returns:
        int: The number of characters written to the file.

    Note:
        - This function overwrites the content of the file if it already exists.
        - If the file does not exist, it will be created.
        - File permissions are not managed by this function.

    Example:
        >>> write_file("example.txt", "Hello, world!")
        13
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print("Error occurred while writing to file: {}".format(e))
        return 0
