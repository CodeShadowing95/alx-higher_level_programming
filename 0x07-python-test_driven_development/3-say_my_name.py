#!/usr/bin/python3
"""
doctest_say_my_name

This function prints My name is <first name> <last name>

>>> say_my_name("John", "Smith")
My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """Returns the first name and last name

    Params:
        first_name: string
        last_name: string

    Raises:
        TypeError if first_name or last_name are not strings
    """
    e1 = "first_name must be a string"
    e2 = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(e1)
    if not isinstance(last_name, str):
        raise TypeError(e2)
    print("My name is {} {}".format(first_name, last_name))
