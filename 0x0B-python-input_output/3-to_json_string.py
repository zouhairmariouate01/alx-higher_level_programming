#!/usr/bin/python3
"""Establishes a function for converting a string to its JSON representation."""
import json


def to_json_string(my_obj):
    """Provides the JSON representation of a given string object."""
    return json.dumps(my_obj)
