#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ele_key, ele_value in sorted(a_dictionary.items()):
        print("{}: {}".format(ele_key, ele_value))
