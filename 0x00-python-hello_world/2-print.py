#!/bin/bash
temp_file=$(mktemp); \
python_code='print(f"\"Programming is like building a multilingual puzzle")'; \
echo "$python_code" > temp_file; \
python3 temp_file; \
rm temp_file
