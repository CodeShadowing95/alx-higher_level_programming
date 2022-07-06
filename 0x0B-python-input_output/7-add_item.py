#!/usr/bin/python3
"""Definition of the function add_item()"""
import sys
import json
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename):
    """add all arguments to a Python list, and save them to a file

    Args:
        filename: JSON file in which the arguments list will be saved
    """
    my_args = sys.argv[1:]
    if not exists(filename):
        save_to_json_file(my_args, filename)
    else:
        tab = load_from_json_file(filename)
        for i in my_args:
            tab.append(i)
        save_to_json_file(tab, filename)


add_item("add_item.json")
