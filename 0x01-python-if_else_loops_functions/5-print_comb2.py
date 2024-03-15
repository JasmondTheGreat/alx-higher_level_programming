#!/usr/bin/python3
for i in range(0, 100):
    lt10 = i < 10
    lt99 = i < 99
    print("{}".format("0" + str(i) if lt10 else i), end="")
    print("{}".format(", " if lt99 else ""), end="")

print()
