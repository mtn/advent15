#!/usr/bin/env python3

from collections import defaultdict
import itertools

nums = []
with open("input.txt") as f:
    for line in f:
        nums.append(int(line.strip()))

container_counts = defaultdict(int)
for sz in range(len(nums)):
    for comb in itertools.combinations(nums, sz):
        if sum(comb) == 150:
            container_counts[sz] += 1

minkey = min(container_counts.keys())
print(container_counts[minkey])

