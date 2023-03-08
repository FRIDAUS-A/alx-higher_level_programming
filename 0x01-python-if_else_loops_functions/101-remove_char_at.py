#!/usr/bin/python3
def remove_char_at(str, n):
    len = len(str)
    i = 0
    while (i < str):
        if (i == n):
            i += 1
            continue
        else:
            tmp[i] = str[i]
        i += 1
    str = tmp

