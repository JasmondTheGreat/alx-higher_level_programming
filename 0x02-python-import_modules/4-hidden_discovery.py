#!/usr/bin/python3.8

import result as my_module

names = dir(my_module)
functions = [name for name in names if callable(getattr(my_module, name))]

if __name__ == "__main__":
    for name in functions:
        if not name.startswith("__"):
            print(name)
