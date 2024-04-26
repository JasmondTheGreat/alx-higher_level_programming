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
        s = self.size
        if not isinstance(s, int):
            raise TypeError("size must be an integer")
        elif s < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return

        for i in range(self.size):
            print("#" * self.size)
