#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    c = len(args)

    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("1 argument:")
        print("1: {}".format(args[0]))
    elif c >= 2:
        print("{} arguments:".format(c))
        for i in range(c):
            print("{}: {}".format(i+1, args[i]))
