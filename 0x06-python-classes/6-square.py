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
    position: tuple
        position of the square

    Methods
    -------
    Constructor():
        if size not an integer or < 0, raise an error with message
        if position not a tuple of 2 integers > 0, raise error with message
    area(self):
        returns the current area of the square
    size(self):
        getter - retrieve the value of an attribute
    size(self, value):
        setter - change the value of an attribute
    my_print():
        print in stdout the square at a given position

    """

    def __init__(self, size=0, position=(0, 0)):     # constructor
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size      # private instance attribute

        if not isinstance(position, tuple) or \
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):                 # getter
        return self.__size

    @size.setter
    def size(self, value):          # setter
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):                 # public instance method
        return self.__size ** 2

    def my_print(self):
        if self.__size != 0:
            """Position on Y axis"""
            if self.__position[1] > 0:
                for _ in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                """Position on X axis"""
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
