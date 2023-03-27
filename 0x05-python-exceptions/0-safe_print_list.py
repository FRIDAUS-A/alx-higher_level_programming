#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for ele in my_list:
        try:
            print(ele, end="")
            if (count < x):
                count += 1
        except IndexError:
            pass
    print()
    return (count)
