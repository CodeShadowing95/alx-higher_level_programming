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
        """
        Constructs all the necessary attributes for the square object

        Parameters
        ----------
        size: int
            size of the square
        position: tuple
            position of the square(X axis, Y axis)
        """
        self.size = size
        self.position = position

    @property
    def size(self):                 # getter
        """
        Getter of size - retrieves the size of the square

        Parameters
        ----------
        None

        Returns
        -------
        The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):          # setter
        """
        Setter of size - change the value of the size of the square

        Parameters
        ----------
        value: int
            size of the square

        Raises:
            TypeError if size is not int
            ValueError if size is less than 0

        Returns
        -------
        None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter of position - retrieves the position of the square

        Parameters
        ----------
        None

        Returns
        -------
        The position of the square(X axis, Y axis)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter of position - change the value of the square' position

        Parameters
        ----------
        value: tuple
            set a position to the square

        Raises:
            TypeError if position is not a tuple, or if any value of the tuple
            is not integer or is less than 0

        Returns
        -------
        None
        """
        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0 or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):                 # public instance method
        """
        Calculate the area of the square

        Parameters
        ----------
        None

        Returns
        -------
        The size of the square multiplied by itself
        """
        return self.__size ** 2

    def my_print(self):
        """
        Display the square at a given position

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.__size != 0:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()
