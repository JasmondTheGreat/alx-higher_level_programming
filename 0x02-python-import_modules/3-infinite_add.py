#!/usr/bin/python3

import sys

argv = sys.argv
argc = len(argv)

if __name__ == "__main__":
    sum = 0

    if (argc - 1) == 0:
        print("0")
    else:
        for i in range(1, argc):
            sum += int(argv[i])
        print("{}".format(sum))
