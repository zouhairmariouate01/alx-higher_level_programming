#!/usr/bin/python3
"""Defines a class Square with private instance attribute size, size validation, area calculation,
and access/update via getter and setter methods."""


class Square:
    """Class Square with private instance attribute size, size validation,
    area calculation, and access/update via getter and setter methods."""
    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.__size = size

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

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
