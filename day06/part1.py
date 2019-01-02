#!/usr/bin/env python3

import re


grid = [[0] * 1000 for _ in range(1000)]
with open("input.txt") as f:
    for line in f:
        topx, topy, bottomx, bottomy = map(int, re.findall("[0-9]+", line))

        for x in range(topx, bottomx+1):
            for y in range(topy, bottomy+1):
                if "turn on" in line:
                    grid[y][x] = 1
                elif "turn off" in line:
                    grid[y][x] = 0
                elif "toggle" in line:
                    grid[y][x] = 0 if grid[y][x] == 1 else 1

ans = 0
for y in range(1000):
    ans += sum(grid[y])
print(ans)


