#!/usr/bin/python3
"""Building of the class Node"""


class Node:
    """
    A class to represent a node
    
    ...

    Attributes
    ----------
    data: int
        the data of the node
    next_node: Node
        next instance of a class Node

    Methods
    -------
    constructor:
        if data is not an integer, raise an error with message
        if next_node is neither None or a Node, raise an error with message
    property getters - data() and next_node()
        retrieves respectively the data and the next instance of Node
    property setters - data(value) and next_node(value)
        set respectively the data of the Node and the next instance of Node

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if next_node != None or type(next_node) != Node:
            raise TypeError("next_node must be a Node object")



"""Building a class SinglyLinkedList"""


class SinglyLinkedList:
    """
    A class that represents a SLL

    ...

    Attributes
    ----------
    head: Node
        represents the current object Node or the object Node at 1st position

    Methods
    -------
    constructor:
        Initializes the SLL
    sorted_insert(value)
        insert a new node into the correct sorted position in the list
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
