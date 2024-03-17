#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

ops = ["+", "-", "*", "/"]
fns = [add, sub, mul, div]

a = 10
b = 5

if __name__ == "__main__":
    for i in range(len(ops)):
        print("{} {} {} = {}".format(a, ops[i], b, fns[i](a, b)))
