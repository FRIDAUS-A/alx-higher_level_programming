#!/usr/bin/python3
if (__name__ == "__main__"):
    import hidden_4
    tmp = dir(hidden_4)
    for ele in tmp:
        if (ele[0] == "_"):
            continue
        print(ele)
