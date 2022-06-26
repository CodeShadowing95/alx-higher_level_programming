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
        """get the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def __lt__(self, other):
        """check if the area square is less than another square

        Args:
            other (Square): square to compare

        Returns:
            bool: True if the area square is less than the other square
        """
        return self.area() < other.area()

    def __le__(self, other):
        """check if the area square is less than or equal to another square

        Args:
            other (Square): square to compare

        Returns:
            bool: True if the area square is less than or
            equal to the other square
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """check if the area square is equal to another square

        Args:
            other (Square): square to compare

        Returns:
            bool: True if the area square is equal to the other square
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """check if the area square is not equal to another square

        Args:
            other (Square): square to compare

        Returns:
            bool: True if the area square is not equal to the other square
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """check if the area square is greater than another square

        Args:
            other (Square): square to compare

        Returns:
            bool: True if the area square is greater than the other square
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """check if the area square is greater than or equal to another square

        Args:
            other (Square): square to compare

        Returns:
            bool: True if the area square is greater than
            or equal to the other square
        """
        return self.area() >= other.area()
