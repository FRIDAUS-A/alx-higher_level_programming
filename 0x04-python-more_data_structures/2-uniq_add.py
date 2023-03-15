#!/usr/bin/python3
def uniq_add(my_list=[]):
    count, result = 0, 0
    new_list = []
    for mem in my_list:
        new_list.append(mem)
    while (count < len(new_list)):
        result = new_list[count] + result
        count1 = count + 1
        while (count1 < len(new_list)):
            if (new_list[count] == new_list[count1]):
                new_list.pop(count1)
            count1 += 1
        count += 1
    return (result)
