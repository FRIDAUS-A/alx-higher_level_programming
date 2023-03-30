#!/usr/bin/python3
"""Define a Square Class"""


class Square:
    """A class named Square"""
    def __init__(self, size=0):
        """Initializes the class Square
            Args:
                size (int): parameter of the init function
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
