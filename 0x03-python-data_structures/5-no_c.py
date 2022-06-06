#!/usr/bin/python3
def no_c(my_string):
    str_list = list()
    for i in my_string:
        if i != 'c' and i != 'C':
            str_list.append(i)
    return ''.join(str_list)
