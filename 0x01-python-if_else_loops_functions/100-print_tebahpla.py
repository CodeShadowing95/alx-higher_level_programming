#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 != 0:
        flag = 32
    else:
        flag = 0
    print("{}".format(chr(i - flag)), end='')
