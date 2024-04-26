#!/usr/bin/python3

""" Creates a class square """


class Square:
    """ Represents a square """

    def __init__(self, size=0):
        """
        Instantiates the class

        Args:
            size (int): size of square
        """
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        finally:
            self.__size = size
