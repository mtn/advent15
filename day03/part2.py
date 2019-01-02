#!/usr/bin/env python3

from collections import defaultdict

visited = { (0,0) }
santax, santay, robox, roboy = 0,0,0,0
with open("input.txt") as f:
    for i, ch in enumerate(f.read().strip()):
        if ch == "^":
            if i % 2 == 0:
                santay += 1
            else:
                roboy += 1
        if ch == "v":
            if i % 2 == 0:
                santay -= 1
            else:
                roboy -= 1
        if ch == ">":
            if i % 2 == 0:
                santax += 1
            else:
                robox += 1
        if ch == "<":
            if i % 2 == 0:
                santax -= 1
            else:
                robox -= 1

        visited.add((santax, santay))
        visited.add((robox, roboy))

print(len(visited))
