#!/usr/bin/python3

""" Defines a class Node """


class Node:
    """ Represents a Node """

    def __init__(self, data, next_node=None):
        """ Instance of Node

            Args:
                data (int): data of node
                next_node (ref): pointer to next node
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        next = self.next_node
        if next is not None or not isinstance(next, object):
            raise TypeError("next_node must be a Node object")


""" Defines a class SinglyLinkedList """


class SinglyLinkedList:
    """ Represents a SinglyLinkedList """
    
    head = Node()
    list = []
    
    def __init__(self):
        """
        Instance of a new linked list

        Args:
            head (object): head node pointer
        """
        self.__head = head
    
    def sorted_insert(self, value):
        for i in range(list):
            if value < list[i]:
                temp = list[i]
                list[i] = value
                list[i + 1] = list[i]

