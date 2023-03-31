#!/usr/bin/python3
"""Defines a class"""


class Square:
    """Defines a class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize class Square.
            Args:
                size (int): param of the init
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieve the attribute position
            Args:
        """
        return self.__position

    @position.setter
    def position(self, value):
        """assign a value to position
            Args:
                value: value of thee position
        """
        if (len(value) != 2 or type(value) != tuple
                or type(value) != int or
                type(value) != int):
            raise TypeError("position must be a tuple of 2 position")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """A method that prints square
            Args:
        """
        count = 0
        [print("") for i in range(0, self.__position[1])]
        if self.__size != 0:
            while (count < self.__size):
                count_in = 0
                count_tmp = 0
                while (count_tmp < self.__position[0]):
                    print(" ", end="")
                    count_tmp += 1
                while (count_in < self.__size):
                    print("#", end="")
                    count_in += 1
                print("")
                count += 1
        else:
            print()
            return
