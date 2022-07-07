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

    def to_json(self, attrs=None):
        """retrieve a dictionary representation of a Student instance"""
        d = dict()
        if attrs is None:
            d = self.__dict__
        else:
            for attr in attrs:
                if attr in list(self.__dict__.keys()):
                    d[attr] = self.__dict__[attr]
        return d

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
