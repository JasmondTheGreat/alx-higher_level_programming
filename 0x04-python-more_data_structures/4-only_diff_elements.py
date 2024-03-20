#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    result = []

    for num1 in set_1:
        common_num_found = False
        for num2 in set_2:
            if num1 == num2:
                common_num_found = True
                break

        if not common_num_found:
            result.append(num1)

    for num2 in set_2:
        common_num_found = False
        for num1 in set_1:
            if num1 == num2:
                common_num_found = True
                break

        if not common_num_found:
            result.append(num2)

    return set(result)
