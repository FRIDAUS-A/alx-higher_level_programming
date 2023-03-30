#!/usr/bin/python3
"""Defines a class"""


class Square:
    """Defines a class Square"""

    def __init__(self, size=0):
        """Initialize class Square.
            Args:
                size (int): param of the init
        """
        self.__size = size

    @property
    def size(self):
        """retrieve the attribute of a function
            Args:
        """
        return self.__size

    @size.setter
    def size(self, value):
        """assign a value to attribute size
            Args:
                value: assign value to size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """A method that prints square
            Args:
        """
        count = 0
        while (count < self.__size):
            count_in = 0
            while (count_in < self.__size):
                print("#", end="")
                count_in += 1
            print()
            count += 1
