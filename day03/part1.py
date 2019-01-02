#!/usr/bin/env python3

from collections import defaultdict

visited = { (0,0) }
curx, cury = 0,0
with open("input.txt") as f:
    for ch in f.read().strip():
        if ch == "^":
            cury += 1
        if ch == "v":
            cury -= 1
        if ch == ">":
            curx += 1
        if ch == "<":
            curx -= 1

        visited.add((curx, cury))

print(len(visited))
