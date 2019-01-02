#!/usr/bin/env python3

from random import shuffle

replacements = []
with open("input.txt") as f:
    replacements_done = False
    for line in f:
        line = line.strip()
        if not line:
            replacements_done = True
            continue

        if not replacements_done:
            splt = line.split(" => ")
            replacements.append((splt[0], splt[1]))
        else:
            in_str = line

# it seems like the only path backwards is also optimal, but we can get stuck
# rather than doing something fancy, just randomize the order we try replacements
# and run in reverse
steps = 0
cur = in_str
while len(cur) > 1:
    initial = cur
    for rfrom, rto in replacements:
        while rto in cur:
            steps += cur.count(rto)
            cur = cur.replace(rto, rfrom)

    if cur == initial:
        shuffle(replacements)
        step = 0

print(steps)
