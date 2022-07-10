#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    s = 0
    for i in range(len(args)):
        s += int(args[i])

    print(s)
