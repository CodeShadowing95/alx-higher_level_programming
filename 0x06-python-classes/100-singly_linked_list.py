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
        """Initializes a new instance of Node

        Args:
            data (int): data to be initialized
            next_node (Node, optional): Points to the next node.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data of the Node

        Returns:
            int: data of the Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the Node

        Args:
            value (int): data to set

        Raises:
            TypeError: if data is not an integer
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the next node of the Node

        Returns:
            Node: the address of the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        If the value is None or a Node, set the next node to the value.
        Otherwise, raise a TypeError.

        :param value: the value of the node
        """
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


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
        """Initializes the linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node into the correct sorted position in the list

        Args:
            value (int): value for the new node
        """
        n = Node(value)

        if self.__head is None:
            n.next_node = None
            self.__head = n
        elif self.__head.data >= value:
            n.next_node = self.__head
            self.__head = n
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node

            n.next_node = current.next_node
            current.next_node = n

    def __str__(self):
        """Define a string representation of this node"""
        val = []
        temp = self.__head
        while temp:
            val.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(val))
