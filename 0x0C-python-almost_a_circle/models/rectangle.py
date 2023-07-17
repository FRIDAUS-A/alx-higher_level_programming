#!/usr/bin/python3
from base import Base
"""Rectangle Class"""

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):

        """Rectangle Class
        Args:
            width (int): width of a class
            height (int): height of a class
            x (int):
            y (int):
        """
        super().__init__(id)
        sel.__width = width
        sel.__height = height
        sel.__x = x
        sel.__y = y
    @property
    def width(self):
        return (self.__width)
    @width.setter
    def width(self, value):
        self.__width = value
    @property
    def height(self):
        return (self.__height)
    @height.setter
    def height(self, value):
        self.__height = value
    @property
    def x(self):
        return (self.__x)
    @x.setter
    def x(self, value):
        self.__x = value
    @property
    def y(self):
        return (self.__y)
    @y.setter
    def y(self, value):
        self.__y = value
