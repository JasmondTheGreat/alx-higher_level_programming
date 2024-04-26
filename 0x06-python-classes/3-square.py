#!/usr/bin/python3

""" Creates a class square """


class Square:
    """ class body """

    def __init__(self, size=0):
        """
        Instantiates a new square

        Args:
            size (int): size property
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
