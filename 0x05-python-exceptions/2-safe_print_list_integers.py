#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    length = 0
    int_count = 0

    if x == 0:
        return

    for num in my_list:
        length = length + 1

    if x > length:
        raise IndexError("list index out of range")

    for i in range(my_list):
        if x == i:
            break
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                int_count = int_count + 1
        except ValueError:
            continue

    return int_count
