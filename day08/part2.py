#!/usr/bin/env python3

ans = 0
with open("input.txt") as f:
    for line in f:
        ans += 2 + line.count("\\") + line.count("\"")
print(ans)
