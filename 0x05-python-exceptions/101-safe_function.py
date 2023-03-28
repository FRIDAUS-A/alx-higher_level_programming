#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        c = fct(*args)
        return (c)
    except Exception:
        return (None)
