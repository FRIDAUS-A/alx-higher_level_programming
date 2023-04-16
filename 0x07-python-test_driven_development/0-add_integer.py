#!/usr/bin/python3
def add_integer(a, b=98):
    """A function that two numbers.
        Args:
                a (int, float): first argument
                b (int, float): second argument
        >>> add_integer(1, 2)
        3
        >>> add_integer(100.3, -2)
        98
    """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    elif (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    else:
        return int((float(a) + float(b)))
