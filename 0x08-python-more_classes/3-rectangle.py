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
        self.__height = height
        if (type(self.__height) != int):
            raise TypeError("height must be an integer")
        if (self.__height < 0):
            raise ValueError("height must be >= 0")
        self.__width = width
        if (type(self.__width) != int):
            raise TypeError("width must be an integer")
        if (self.__width < 0):
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """defines the getter for the attributes of the object
            Args:
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """defines the setter for the object attribute
            Args:
                value (int): set the width attibute to value
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """defines the getter for the attributes of the object
            Args:
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """defines the setter for the height attribute of the object
            Args:
                value (int): set the height attribute of the object to height
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """A method to calculate the area of the rectangle
            Args:
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """A method to calculate the perimeter of the rectangle
            Args:
        """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """str method that defines the definition of the object
            Args:
        """
        y = self.__height
        x = self.__width
        tmp_stor = []
        stor = ""
        while (y > 0):
            x = self.__width
            while (x > 0):
                tmp_stor.append("#")
                x -= 1
            if (y != 1):
                tmp_stor.append("\n")
            y -= 1
        for ele in tmp_stor:
            stor += ele
        return (stor)
