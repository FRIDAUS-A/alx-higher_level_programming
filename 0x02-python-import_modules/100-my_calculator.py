#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    import calculator_1
    if (not (len(argv) - 1 == 3)):
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        print()
    if (not (argv[2] == "+" or argv[2] == "-" or argv[2] == "*" or argv[2] == "/")):
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
        print()
    elif (argv[2] == "+"):
        result = calculator_1.add(int(argv[1]), int(argv[3]))
    elif (argv[2] == "-"):
        result = calculator_1.sub(int(argv[1]), int(argv[3]))
    elif (argv[2] == "*"):
        result = calculator_1.mul(int(argv[1]), int(argv[3]))
    elif (argv[2] == "/"):
        result = calculator_1.div(int(argv[1]), int(argv[3]))
    if (argv[2] == "+" or argv[2] == "-" or argv[2] == "*" or argv[2] == "/"):
        print(f"{argv[1]} {argv[2]} {argv[3]} = {result:d}")
