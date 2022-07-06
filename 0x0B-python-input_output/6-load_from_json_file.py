#!/usr/bin/python3
"""Definition of the function load_from_json_file()"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file

    Args:
        filename: file to operate on
    """
    with open(filename) as f:
        return json.load(f)
