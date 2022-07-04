#!/usr/bin/python3

"""Definition of the function lookup()"""


def lookup(obj):
    """Return the list of available attributes and methods of obj

    Args:
        obj: object to operate on
    """

    return dir(obj)
