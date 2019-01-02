#!/usr/bin/env python3

floor = 0
with open("input.txt") as f:
    inp = f.read().strip()
    for i, ch in enumerate(inp):
        if ch == "(":
            floor += 1
        else:
            assert ch == ")"
            floor -= 1

            if floor == -1:
                print(i + 1)
                exit()

