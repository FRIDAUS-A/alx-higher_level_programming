#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    count = 0
    while (count < len(my_list)):
        if (my_list[count] == search):
            new_list.append(replace)
        else:
            new_list.append(my_list[count])
        count += 1
    return (new_list)
