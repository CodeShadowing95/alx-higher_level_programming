#!/usr/bin/python3

def weight_average(my_list=[]):
    s1, s2 = 0, 0

    if len(my_list) == 0:
        return (0)
    for i in range(len(my_list)):
        s1 += (my_list[i][0] * my_list[i][1])
        s2 += my_list[i][1]

    return (s1 / s2)
