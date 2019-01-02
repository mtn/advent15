#!/usr/bin/env python3

import re

total = 0
with open("input.txt") as f:
    for line in f:
        ll = [l, w, h] = list(map(int, re.findall("[0-9]+", line)))
        per = 2 * ll[0] + 2 * ll[1]
        total += per
        total += l * w * h
print(total)

