#!/usr/bin/python3
# 6-from_json_string.py
"""Creates a function for converting JSON to a Python object."""
import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string."""
    return json.loads(my_str)
