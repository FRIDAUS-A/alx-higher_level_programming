#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    print("{} argument:".format(len(argv)))
    count = 1
    while (count < len(argv)):
        print("{:d}: {}".format(count, argv[count]))
        count = count + 1
