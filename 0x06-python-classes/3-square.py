#!/usr/bin/python3
"""Defines a class Square with private instance attribute size, size validation, and area calculation."""


class Square:
    """Class Square with private instance attribute size, size validation, and area calculation."""
    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
