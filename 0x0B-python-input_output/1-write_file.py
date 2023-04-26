#!/usr/bin/python3
"""WRITING A STRING TO THE END OF TEXTFILE"""


def append_write(filename="", text=""):
    """APPEND TO THE END OF A FILE.
        Args:
            filename(string): name of file
            text(string): text
    """
    with open(filename, "a") as file:
        file.append(text)
    return (len(text))
