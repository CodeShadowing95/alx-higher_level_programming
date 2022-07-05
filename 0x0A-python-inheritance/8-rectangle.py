#!/usr/bin/python3
"""Definition of the class Rectangle inheriting BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to represent any rectangle"""
    def __init__(self, width, height):
        """Initializes an object of the class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
