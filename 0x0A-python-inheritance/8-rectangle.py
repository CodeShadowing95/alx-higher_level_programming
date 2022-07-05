#!/usr/bin/python3
"""Definition of the class BaseGeometry"""


class BaseGeometry:
    """A class to represent any geometry"""
    def integer_validator(self, name, value):
        """checks whether value is an integer or not

        Args:
            name: string
            value: value to be checked

        Raises:
            TypeError if the value is not an integer
            ValueError if the value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """raise an Exception with a message"""
        raise Exception("area() is not implemented")


"""Definition of the class Rectangle"""


class Rectangle(BaseGeometry):
    """A class to represent any rectangle"""
    def __init__(self, width, height):
        """Initializes an object of the class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
