#!/usr/bin/python3
"""Definition of the function append_write()"""


def append_write(filename="", text=""):
    """append a string at the end of a text file and
    returns the number of cg=hars added

    Args:
        filename: file to operate on
        text: text to add at end of the file
    """
    with open(filename, 'a+', encoding='UTF-8') as f:
        return f.write(text)
