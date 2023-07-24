#!/usr/bin/python3
"""Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """A Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """Rectangle Class
        Args:
            width (int): width of a class
            height (int): height of a class
            x (int):
            y (int):
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x of the rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y of the rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """displays the character '#'"""
        for height in range(self.__height):
            [print() for line in range(self.__y) if height == 0]
            [print(" ", end="") for space in range(self.__x)]
            [print('#', end="") for mem in range(self.__width)]
            print()

    def __str__(self):
        """defines the object"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns argument to each attribute"""
        if (len(args) != 0):    
            if (len(args) >= 1):
                self.id = args[0]
            if (len(args) >= 2):
                self.__width = args[1]
            if (len(args) >= 3):
                self.__height = args[2]
            if (len(args) >= 4):
                self.__x = args[3]
            if (len(args) >= 5):
                self.__y = args[4]
        else:
            for key,value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "height":
                    self.__height = value
                elif key == "width":
                    self.__width = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict = {'x': self.__x, 'y': self.__y, 'id': self.id, 'height': self.__height, 'width': self.__width}
        return dict
