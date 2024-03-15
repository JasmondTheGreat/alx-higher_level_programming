#!/usr/bin/python3
for i in range(0, 100):
    print("{}".format("0" + str(i) if i < 10 else i), end="")
    print("{}".format(", " if i != 99 else "\n"), end="")
