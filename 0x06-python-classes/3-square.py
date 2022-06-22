#!/usr/bin/python3
"""Building of the class Square"""


class Square:
    """
    A class to represent any square.

    ...

    Attributes
    ----------
    size: int
        size of the square

    Methods
    -------
    Constructor():
        if size not an integer or less than 0, raise an error with message
    area():
        returns the current area of the square

    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size      # private instance attribute

    def area(self):             # public instance method
        return self.__size ** 2
