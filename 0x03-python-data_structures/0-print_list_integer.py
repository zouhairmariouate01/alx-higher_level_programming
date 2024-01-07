#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
"""Print all integers of a list."""
    for num in my_list:
        print(str.format("{0}", num))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
