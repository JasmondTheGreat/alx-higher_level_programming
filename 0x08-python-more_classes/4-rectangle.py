#!/usr/bin/python3

""" Defines a class Rectangle """


class Rectangle:
    """ Represents a Rectangle """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.height + self.width)

    def __str__(self) -> str:
        result_str = ''

        if self.height == 0 or self.width == 0:
            return ''

        for _ in range(self.height):
            result_str += '#' * self.width + '\n'

        return result_str

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
