#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len = len(my_list) - 1
    while (len):
        print("{:d}".format(my_list[len]))
        len = len - 1
