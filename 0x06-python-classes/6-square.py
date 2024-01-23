#!/usr/bin/python3
"""Defines a class Square with private instance attributes size, position,
size validation, area calculation, access/update via getter and setter methods,
and printing the square."""


class Square:
    """Class Square with private instance attributes size, position,
    size validation, area calculation, access/update via getter and setter methods,
    and printing the square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or if position values are less than 0.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute.

        Args:
            value (tuple): The position values to set.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If position values are less than 0.

        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character # and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

