#!/usr/bin/python3

def pow(a, b):
    result = 1

    for i in range((-1 * b) if b < 0 else b):
        result *= a

    if (b < 0):
        result = 1 / result

    return result
