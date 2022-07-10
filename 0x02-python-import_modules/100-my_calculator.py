#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    t = sys.argv[1:]
    if len(t) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(t[0])
        b = int(t[2])
        if t[1] not in "+-*/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if t[1] == "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif t[1] == "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif t[1] == "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            elif t[1] == "/":
                print("{} / {} = {}".format(a, b, div(a, b)))
