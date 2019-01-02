#!/usr/bin/env python3

import re

nice = 0
with open("input.txt") as f:
    for line in f:
        word = line.strip()

        repeating = re.search(r'(..).*\1', word, re.I)
        between = re.search(r'(.).\1', word, re.I)

        if repeating and between:
            nice += 1

print(nice)

