#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = -1
    stop = -1 * len(my_list)
    while (count >= stop):
        print("{:d}".format(my_list[count]))
        count = count - 1
