#!/usr/bin/python3
"""Definition of the function save_to_json_file()"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation

    Args:
        my_obj: the object to operate on
        filename: file in which my_obj will be stored in JSON repr.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
