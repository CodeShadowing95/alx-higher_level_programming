#!/usr/bin/python3
"""Building of MagicCLass"""
import math


class MagicClass:
    """Representation of the MagicClass according to the bytecode"""

    def __init__(self, radius=0):
        """Initialize class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """calculates the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """calculates the perimeter of the circle"""
        return (2 * math.pi) * self.__radius
