#!/usr/bin/python3
""" a function that returns the list of
available attributes and methods of an object:
"""


def lookup(obj):
    """returns the list of available names
        Args:
            obj (object): object of a class
    """
    return (dir(obj))
