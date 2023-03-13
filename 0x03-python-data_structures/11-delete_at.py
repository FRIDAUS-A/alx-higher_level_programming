#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0 or idx >= len(my_list)):
        return (my_list)
    else:
        new_list = []
        for mem in my_list:
            new_list.append(mem)
        new_list.remove(new_list[idx])
        my_list = new_list
        return (new_list)
