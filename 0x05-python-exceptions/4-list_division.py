#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    itr = 0
    itr_2 = 0
    new_list = []
    while (itr < list_length):
        while (itr_2 < list_length):
            try:
                result = my_list_1[itr] / my_list_2[itr_2]
                new_list.append(result)
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except IndexError:
                new_list.append(0)
                print("out of range")
            finally:
                itr_2 += 1
                break
        itr += 1
    return (new_list)
