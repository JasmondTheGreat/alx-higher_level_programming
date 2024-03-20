#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_list = []
    for key in a_dictionary:
        sorted_list.append(key)

    sorted_list.sort()

    for sorted_key in sorted_list:
        print("{}: {}".format(sorted_key, a_dictionary[sorted_key]))
