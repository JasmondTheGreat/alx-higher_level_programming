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

    def area(self):
        """
        Calcs the area

        Returns:
            int: the area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Gets the size

        Returns:
            int: the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size
        """
        self.__size = value

