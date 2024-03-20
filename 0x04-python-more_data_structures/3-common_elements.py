#!/usr/bin/python3

def common_elements(set_1, set_2):
    result = []

    for num1 in set_1:
        for num2 in set_2:
            if num1 == num2:
                result.append(num1)
                break

    return set(result)
