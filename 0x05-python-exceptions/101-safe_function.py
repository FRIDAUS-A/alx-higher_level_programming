#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        c = fct(*args)
        return (c)
    except (ValueError, NameError, ZeroDivisionError, TypeError, IndexError) as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return (None)
