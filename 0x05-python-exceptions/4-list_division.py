#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    tab = []
    for i in range(list_length):
        try:
            n = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            n = 0
        except (ValueError, TypeError):
            print("wrong type")
            n = 0
        except IndexError:
            print("out of range")
            n = 0
        finally:
            tab.append(n)
    return tab
