#!/usr/bin/python3
"""The square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """The class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """defines the atrribute of the class insatnce
        Args:
            size (int): size of the square
            x (int): position x of the square
            y (int): position y of the square
            id (int): object id
        """
        self.__size = size
        self.__x = x
        self.__y = y
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for the size"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if (value <= 0):
            raise ValueError("size must be > 0")
        else:
            self.__size = value

    def __str__(self):
        """return thr string representation of an object"""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}"

    def update(self, *args, **kwargs):
        """update the attributes"""
        if (len(args) != 0):
            if (len(args) >= 1):
                self.id = args[0]
            if (len(args) >= 2):
                self.__size = args[1]
            if (len(args) >= 3):
                self.__x = args[2]
            if (len(args) >= 4):
                self.__y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.__size = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dict = {'id': self.id, 'x': self.__x,
                'size': self.__size, 'y': self.__y}
        return dict
