#!/usr/bin/env python3

import re

def compute_next(cur):
    return (cur * 252533) % 33554393

def to_ind(row, col):
    return sum(range(row + col- 1)) + col

with open("input.txt") as f:
    row, col = map(int, re.findall("[0-9]+", f.read()))

steps = to_ind(row, col)

cur = 20151125
for i in range(steps - 1):
    cur = compute_next(cur)

print(cur)
