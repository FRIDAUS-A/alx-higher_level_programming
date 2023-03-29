#!/usr/bin/python3
"""defines a class Square with size as a private attribute"""


class Square:
    """Represent a Square"""
    def __init__(self, size):
        """Ïnitializes a Square.
            Args:
                size: the attribute of the Square
        """
        self.__size = size
