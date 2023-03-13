#!/usr/bin/python3
def max_integer(my_list=[]):
    count = 0
    if (len(my_list) == 0):
        return (None)
    test = my_list[0]
    while (count < len(my_list)):
        if (test < my_list[count]):
            test = my_list[count]
        count += 1
    return (test)
