#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as tve:
        # print("Exception: {}".format(tve), file=sys.stderr)
        sys.stderr.write("Exception: {}".format(tve))
        return False
