#!/usr/bin/python3
"""THE BASE CLASS"""


class Base:
    """Base class for other classes"""
    _nb_objects = 0
    def __init__(self, id=None):
        """constructor
            Args:
                id (int): id for the class
        """
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
