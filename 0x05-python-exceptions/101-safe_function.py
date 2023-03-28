#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        c = fct(*args)
        return (c)
    except (ValueError, NameError, ZeroDivisionError, TypeError, IndexError):
        return (None)
