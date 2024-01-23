#!/usr/bin/python3
"""Defines a class Square with private instance attribute size and size validation."""


class Square:
    """Class Square with private instance attribute size and size validation."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
