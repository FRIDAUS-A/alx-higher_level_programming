#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    if (len(argv) - 1 == 0):
        str = "arguments."
    elif (len(argv) - 1 == 1):
        str = "argument:"
    else:
        str = "arguments:"
    print("{} {}".format(len(argv) - 1, str))
    count = 1
    while (count < len(argv)):
        print("{:d}: {}".format(count, argv[count]))
        count = count + 1
