#!/usr/bin/python3

def safe_print_integer(value):
    if isinstance(value, int):
        try:
            print("{:d}\n".format(value))
            return True
        except TypeError:
            return False
