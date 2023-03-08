#!/usr/bin/python3
small, capital = 25, 9
for alp in range(97, 123):
    if (alp % 2 == 0):
        alp = alp - capital
        print("{:c}".format(alp), end="")
        alp = alp + capital
        capital = capital + 4
    else:
        alp = alp + small
        print("{:c}".format(alp), end="")
        alp = alp - small
        small = small - 4
