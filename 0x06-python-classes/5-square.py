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
    area(self):
        returns the current area of the square
    size(self):
        getter - retrieve the value of an attribute
    size(self, value):
        setter - change the value of an attribute
    my_print():
        print in stdout the square

    """

    def __init__(self, size=0):     # constructor
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size      # private instance attribute

    @property
    def size(self):                 # getter
        return self.__size

    @size.setter
    def size(self, value):          # setter
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):                 # public instance method
        return self.__size ** 2

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
