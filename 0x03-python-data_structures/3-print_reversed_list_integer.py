#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = -1
    stop = (-1) * len(my_list)
    new_list = []
    while (count >= stop):
        new_list.append(my_list[count])
        count = count - 1
    my_list = new_list
    for mem in my_list:
        print("{:d}".format(mem))
    return (my_list)
