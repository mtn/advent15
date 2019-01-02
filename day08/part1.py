#!/usr/bin/env python3

ans = 0
with open("input.txt") as f:
    for line in f:
        ans += len(line[:-1]) - len(eval(line))
print(ans)
