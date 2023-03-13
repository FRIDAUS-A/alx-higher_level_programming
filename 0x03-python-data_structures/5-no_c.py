#!/usr/bin/python3
def no_c(my_string):
    count = 0
    my_string_tmp = ""
    my_string = list(my_string)
    while (count < len(my_string) - 1):
        if (my_string[count] == 'c' or my_string[count] == 'C'):
            if (my_string[count] == 'C'):
                my_string[count] = ' '
            else:
                my_string.remove(my_string[count])
        count = count + 1
    for mem in my_string:
        my_string_tmp += mem
    my_string = my_string_tmp
    return (my_string)
print(no_c("Best School"))
