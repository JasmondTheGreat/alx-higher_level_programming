#!/usr/bin/python3

""" Defines a class Square """


class Square:
    """ Represents a Square """

    def __init__(self, size=0):
        """ Instantiates a new Square

            Args:
                size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        else:
            return self.size ** 2
