#!/usr/bin/python3

""" Defines a class Square """


class Square:
    """ Represents a Square """

    def __init__(self, size=0, position=(0, 0)):
        """ Instantiates a new Square

            Args:
                size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        p = position.value
        if not isinstance(p, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return

        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print("_" * self.position[0], end="")
            print("#" * self.size)
