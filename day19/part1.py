#!/usr/bin/env python3

from collections import defaultdict

replacements = set()
with open("input.txt") as f:
    replacements_done = False
    for line in f:
        line = line.strip()
        if not line:
            replacements_done = True
            continue

        if not replacements_done:
            splt = line.split(" => ")
            replacements.add((splt[0], splt[1]))
        else:
            in_str = line

seen = set()
for rfrom, rto in replacements:
    for i in range(len(in_str)):
        if in_str[i: i + len(rfrom)] == rfrom:
            seen.add(in_str[:i] + rto + in_str[i+len(rfrom):])
print(len(seen))

