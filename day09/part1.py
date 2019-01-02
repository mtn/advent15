#!/usr/bin/env python3

from collections import defaultdict
from itertools import permutations

g = defaultdict(dict)
with open("input.txt") as f:
    for line in f:
        start_end, cost = line.split(" = ")
        start, end = start_end.split(" to ")

        g[start][end] = int(cost)
        g[end][start] = int(cost)

shortest_distance = 100000
for path in permutations(g.keys()):
    dist = 0
    for start, end in zip(path, path[1:]):
        dist += g[start][end]
    shortest_distance = min(shortest_distance, dist)
print(shortest_distance)
