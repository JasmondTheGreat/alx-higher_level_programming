#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
unsigned_number = (number * -1) if number < 0 else number
last_digit = unsigned_number % 10

if (number < 0):
    last_digit *= -1

if last_digit == 0:
    last_digit_info = "0"
elif last_digit < 6:
    last_digit_info = "less than 6 and not 0"
elif last_digit > 5:
    last_digit_info = "greater than 5"

print(f"Last digit of {number} is {last_digit} and is {last_digit_info}")
