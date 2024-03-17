#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

argv = sys.argv
argc = len(argv)

ops = ["+", "-", "*", "/"]
fns = [add, sub, mul, div]
op_found = 0

"""
calculator = [
    ["+", add],
    ["-", sub],
    ["*", mul],
    ["/", div]
]
"""

if __name__ == "__main__":
    if not argc - 1 == 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]

        for i in range(0, len(ops)):
            if str(ops[i]) == str(operator):
                print("{} {} {} = {}".format(a, operator, b, fns[i](a, b)))
                op_found = 1

        if (op_found == 0):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
