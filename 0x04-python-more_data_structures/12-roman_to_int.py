#!/usr/bin/python3

def roman_to_int(roman_string):
    sum = 0

    mapping = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    if not roman_string or not isinstance(roman_string, str):
        return 0

    for i in range(len(roman_string)):
        if (i + 1) <= len(roman_string) - 1:
            if roman_string[i] == 'I':
                if roman_string[i + 1] == 'V' or roman_string[i + 1] == 'X':
                    sum -= 1
                    continue
            elif roman_string[i] == 'X':
                if roman_string[i + 1] == 'L' or roman_string[i + 1] == 'C':
                    sum -= 10
                    continue
            elif roman_string[i] == 'C':
                if roman_string[i + 1] == 'D' or roman_string[i + 1] == 'M':
                    sum -= 100
                    continue

        sum += mapping[roman_string[i]]

    return sum
