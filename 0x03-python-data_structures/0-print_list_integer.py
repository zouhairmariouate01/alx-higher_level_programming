#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in my_list:
        print(str.format("{0}", num))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
