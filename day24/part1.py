#!/usr/bin/env python3

from itertools import combinations

nums = []
with open("input.txt") as f:
    for line in f:
        nums.append(int(line.strip()))

per_group = sum(nums) // 3

# try to find the smallest subset summing to this; see if it's correct
# bad in general

for n in range(len(nums)):
    sub = [l for l in list(combinations(nums, n)) if sum(l) == per_group]
    if len(sub) > 0:
        break

ans = 1
for i in sub[0]:
    ans *= i
print(ans) # well, it worked
