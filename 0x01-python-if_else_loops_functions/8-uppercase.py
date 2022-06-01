#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            flag = 32
        else:
            flag = 0
        print("{}".format(chr(ord(str[i]) - flag)), end='')
    print()
