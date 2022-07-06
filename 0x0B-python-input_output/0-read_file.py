#!/usr/bin/python3
"""Definition of the function read_file()"""


def read_file(filename=""):
    """read a text file and print it to stdout

    Args:
        filename: file to operate on
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
