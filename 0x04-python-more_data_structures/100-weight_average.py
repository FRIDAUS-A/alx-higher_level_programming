#!/usr/bin/python3
def weight_average(my_list=[]):
    if (my_list is None or my_list == []):
        return (0)
    total, freq = 0, 0
    for mem in my_list:
        total = mem[0] * mem[1] + total
        freq = mem[1] + freq
    return (total / freq)
