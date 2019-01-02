#!/usr/bin/env python3

import re

total = 0
with open("input.txt") as f:
    for line in f:
        l, w, h = map(int, re.findall("[0-9]+", line))
        total += 2*(l*w + w*h + h*l)
        total += l * w * h // max(l, w, h)
print(total)

