#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 or idx >= len(my_list)):
        return (my_list)
    else:
        new_list = []
        for mem in my_list:
            new_list.append(mem)
        new_list[idx] = element
        return (new_list)
