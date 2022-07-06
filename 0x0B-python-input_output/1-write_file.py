#!/usr/bin/python3
"""Definition of the function write_file()"""


def write_file(filename="", text=""):
    """write a string to a text file and returns the number of characters
    written

    Args:
        filename: file to operate on
        text: text to write in the file
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
