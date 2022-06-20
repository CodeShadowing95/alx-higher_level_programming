#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        d = a / b
        return d
    except ZeroDivisionError:
        d = "None"
        return d
    finally:
        print("Inside result: {}".format(d))
