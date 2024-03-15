#!/usr/bin/python3
alphabets = ""
for i in range(97, 123):
    if chr(i) == "q" or chr(i) == "e":
        continue
    alphabets += "{}".format(chr(i))

print(alphabets, end="")
