#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    length = 0
    check = 0
    for ele in my_list:
            length += 1
    while (check < x):
        try:
            if (count < x):
                print("{:d}".format(my_list[check]), end="")
                count += 1
        except (ValueError, TypeError, NameError):
            pass
        check += 1
    print()
    return (count)
