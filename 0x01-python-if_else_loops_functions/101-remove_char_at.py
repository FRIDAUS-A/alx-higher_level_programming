#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = str
    str1 = list(str1)
    if (not (n < 0) and n < len(str1)):
        str1[n] = ''
    tmp = ""
    for mem in str1:
        tmp += mem
    return (tmp)
print(remove_char_at("School", 10))
