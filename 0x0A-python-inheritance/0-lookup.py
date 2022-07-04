#!/usr/bin/python3

def lookup(obj):
    """Get the list of available attributes and methods of an object

    Args:
    obj (Object): an object

    Returns:
    list
    """
    return dir(obj)
