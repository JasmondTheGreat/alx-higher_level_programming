#!/usr/bin/python3

import sys
argc = len(sys.argv)
argv = sys.argv

if argc == 1:
    print("0 arguments.")
else:
    print("{} argument{}:".format(argc - 1, "" if argc == 2 else "s"))

    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
