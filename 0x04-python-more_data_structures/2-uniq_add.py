#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    unique_list = []

    # create the unique list of numbers
    for num in my_list:
        number_found = False

        for unique_num in unique_list:
            if num == unique_num:
                number_found = True
                break

        if not number_found:
            unique_list.append(num)

    # sum up the unique numbers
    for num in unique_list:
        sum += num

    return sum
