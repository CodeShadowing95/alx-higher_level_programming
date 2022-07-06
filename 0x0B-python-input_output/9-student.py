#!/usr/bin/python3
"""Building of the class Student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize an instance of Student with first_name, last_name
        and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
