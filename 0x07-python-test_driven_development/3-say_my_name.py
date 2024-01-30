#!/usr/bin/python3
"""
This module is named "3-say_my-name."
The "3-say_my_name" module provides a single function called say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """Outputs "My name is" followed by the first name and, if provided, the optional last name."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
