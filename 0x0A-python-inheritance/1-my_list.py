#!/usr/bin/python3
"""Building of the class MyList"""


class MyList(list):
    """Subclass of the class list"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
