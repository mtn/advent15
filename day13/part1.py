#!/usr/bin/env python3

import re
from collections import defaultdict
from itertools import permutations

dhs = defaultdict(dict) # dh of fst sitting next to snd
names = set()
with open("input.txt") as f:
    for line in f:
        dh = int(re.findall("[0-9]+", line)[0])
        if "lose" in line:
            dh *= -1

        words = line.split()
        fst, snd = words[0], words[-1][:-1]
        dhs[fst][snd] = dh

        names.add(fst)
        names.add(snd)

best_dh = -1000
for perm in permutations(names):
    dh = 0
    for i, person in enumerate(perm):
        dh += dhs[person][perm[i-1]]
        dh += dhs[person][perm[(i+1) % len(perm)]]
    best_dh = max(best_dh, dh)
print(best_dh)


