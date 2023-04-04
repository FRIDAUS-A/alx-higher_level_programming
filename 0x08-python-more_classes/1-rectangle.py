#!/usr/bin/python3
"""A module that defines a class Rectangle"""


class Rectangle:
    """Defines a class Rectangle"""
    def __init__(self, width=0, height=0):
        """Defines a constructor for the class
            Args:
                width (int): repr the width of the object
                height (int): repr the width of the object
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
