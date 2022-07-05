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

    def area(self):
        """Returns the area of the rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
