#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list) - 1
    while (count >= 0):
        print("{:d}".format(my_list[count]))
        count = count - 1
