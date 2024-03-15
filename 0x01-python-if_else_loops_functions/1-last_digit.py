#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = '-' if number < 0 else ''
unsigned_number = (number * -1) if number < 0 else number
print(f"Last digit of {number} is {sign}{unsigned_number % 10}")
