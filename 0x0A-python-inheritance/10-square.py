#!/usr/bin/python3
"""Definition of the class Square that inherits Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """initializes an instance of Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """get the area of the Square through his size

        Args:
            size (int): size of a square
        """
        return self.__size ** 2
