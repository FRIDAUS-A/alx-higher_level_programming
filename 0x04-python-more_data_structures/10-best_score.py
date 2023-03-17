#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None):
        return (None)
    for ele in list(a_dictionary.values()):
        count = 0
        for sub_ele in list(a_dictionary.values()):
            if (ele >= sub_ele):
                count += 1
                continue
            else:
                break
        if (count == len(a_dictionary)):
            break
    for key, value in a_dictionary.items():
        if (ele == value):
            return (key)
    return (None)
