#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if x == 0:
        print("{}".format(my_list[x]))
        return 1
    elif x > 0:
        try:
            for i in range(x):
                print("{}".format(my_list[i]), end="")
                count += 1
            print()
        except Exception:
            print()
    return count
