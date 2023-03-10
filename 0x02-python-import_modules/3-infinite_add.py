#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    count = 1
    result = 0
    while (count < len(argv)):
        result = result + int(argv[count])
        count = count + 1
    print(result)
