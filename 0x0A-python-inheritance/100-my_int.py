#!/usr/bin/python3
"""Building of the class MyInt that inherits int"""


class MyInt(int):
    """class MyInt"""
    def __ne__(self, other):
        """redefine not equal method"""
        return self.__getattribute__ != other.__getattribute__

    def __eq__(self, other):
        """redefine equal method"""
        return self.__getattribute__ == other.__getattribute__
