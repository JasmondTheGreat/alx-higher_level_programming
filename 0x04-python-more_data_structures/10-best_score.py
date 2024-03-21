#!/usr/bin/python3

def best_score(a_dictionary):
    max = 0
    max_key = ''

    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > max:
                max = a_dictionary[key]
                max_key = key
    else:
        return None

    return max_key
