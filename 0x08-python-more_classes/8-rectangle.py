#!/usr/bin/python3
"""Building of a class Rectangle defining a rectangle"""


class Rectangle:
    """
    A class to represent any rectangle

    ...

    Attributes
    ----------
    width: int
        width of the rectangle
    height: int
        height of the rectangle

    Methods
    -------
    constructor:
        initialize the object Rectangle
    width():
        getter and setter
    height():
        getter and setter
    area():
        calculates the area of the rectangle
    perimeter():
        calculates the perimeter of the rectangle
    print() - str():
        print the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize an instance of the class Rectangle
        with width and height

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """get the width of the Rectangle

        Returns:
            width (int): the width of the Rectangle object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle

        Args:
            value (int): the width of the rectangle to set

        Raises:
            TypeError if width is not an integer
            ValueError if width less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle

        Returns:
            height (int): the height of the rectangle object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle

        Args:
            value (int): the height of the rectangle to set

        Raises:
            TypeError if height is not an integer
            ValueError if height less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle

        Returns:
            int: 0 if width or height equal 0,
            otherwise area of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of the rectangle

        Returns:
            int: 0 if width or height equal 0,
            otherwise perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """string representation of the object Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        tab = []
        for _ in range(self.__height):
            tab.append("{}".format(self.print_symbol) * self.__width)
        return "\n".join(tab)

    def __repr__(self):
        """internal representation of an object. A string which can be parsed
        by the python interpreter"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """destroy any instance of Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method that checks whether a class Rectangle is bigger than
        or equal to another class Rectangle

        Args:
            rect_1 (Rectangle): class1
            rect_2 (Rectangle): class 2

        Returns:
            rect_1 if the area of both rectangles have the same value

        Raises:
            TypeError if rect_1 or rect_2 are not instances od Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() <= rect_2.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            return rect_1
