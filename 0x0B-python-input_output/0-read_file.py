#!/usr/bin/python3
"""Creates a function that reads text files."""


def read_file(filename=""):
    """Display the contents of a UTF-8 encoded text file on the standard output (stdout)."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
