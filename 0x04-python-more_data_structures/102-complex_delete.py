#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (a_dictionary is None):
        return (None)
    my_key = []
    for key, val in a_dictionary.items():
        if val == value:
            my_key.append(key)
    for mem_1 in my_key:
        a_dictionary.pop(mem_1, None)
    return (a_dictionary)
