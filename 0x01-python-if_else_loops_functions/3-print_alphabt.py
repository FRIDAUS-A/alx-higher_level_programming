#!/usr/bin/python3
for alp in range(97, 122):
    if (not (alp == 101) and not (alp == 113)):
        print("{:c}".format(alp), end="")
