#!/usr/bin/python3
"""A FUNCTION THAT READS FROM A TEXT FILE"""


def read_file(filename=""):
    """ READ FROM A TEXT FILE.
        Args:
            filename(string): name of file
    """
    with open(filename, "r") as file:
        print(file.read())
