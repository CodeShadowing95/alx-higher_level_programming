#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == "" or key not in list(a_dictionary.keys()):
        return a_dictionary
    del(a_dictionary[key])
    return a_dictionary
