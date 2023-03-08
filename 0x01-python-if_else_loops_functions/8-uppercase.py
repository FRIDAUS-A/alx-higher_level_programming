#!/usr/bin/python3
def uppercase(str):
    for mem in str:
        if (ord(mem) >= 97 and ord(mem) <= 122):
            mem = ord(mem) - 32
        else:
            mem = ord(mem)
        print("{:c}".format(mem), end="")
    print()
