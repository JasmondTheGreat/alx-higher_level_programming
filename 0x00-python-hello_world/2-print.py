#!/bin/bash
temp_file=$(mktemp); echo "print(f'\"Programming is like building a multilingual puzzle')" > temp_file; python3 temp_file; rm temp_file
