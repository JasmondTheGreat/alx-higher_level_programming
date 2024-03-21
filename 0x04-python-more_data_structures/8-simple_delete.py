#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    key_exists = False

    for k in a_dictionary:
        if k == key:
            key_exists = True
            break

    if key_exists:
        del a_dictionary[key]

    return a_dictionary
