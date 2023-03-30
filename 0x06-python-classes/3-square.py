#!/usr/bin/python3
"""Defines a class Square Class"""

class Square:
    """A class Square"""

    def __init__(self, size=0):
        """Initializes a class Square.
            Args:
                size (int): param of the function
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """Initializes the method area.
            Args:
        """
        return self.__size ** 2
