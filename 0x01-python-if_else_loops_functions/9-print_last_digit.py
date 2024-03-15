#!/usr/bin/python3

def print_last_digit(number):
    unsigned_num = (-1 * number) if number < 0 else number
    last_dig = unsigned_num % 10

    print("{}".format(last_dig), end="")

    return last_dig
