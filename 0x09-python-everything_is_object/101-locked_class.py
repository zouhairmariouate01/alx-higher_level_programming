#!/usr/bin/python3
"""Specifies a class with lock functionality."""


class LockedClass:
    """
    Disallow the instantiation of new attributes for the LockedClass.
    except for those named 'first_name'.
    """

    __slots__ = ["first_name"]
