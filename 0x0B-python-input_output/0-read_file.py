#!/usr/bin/python3
"""Definition of the functionread_file()"""


def read_file(filename=""):
    """read a text file and print it out to stdout
    
    Args:
        filename: file to operate on
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
