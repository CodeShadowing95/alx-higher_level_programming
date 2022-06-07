#!/usr/bin/python3
def max_integer(my_list=[]):
    imax = 0
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)-1):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                imax = my_list[i] if my_list[i] > imax else imax
            else:
                imax = my_list[j] if my_list[j] > imax else imax
    return imax
