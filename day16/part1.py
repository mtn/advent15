#!/usr/bin/env python3

import re

ticker = {}
with open("ticker.txt") as f:
    for line in f:
        splt = line.strip().split(": ")
        ticker[splt[0]] = int(splt[1])

sues = []
with open("input.txt") as f:
    for line in f:
        after = line[line.index(":") + 2:]
        dct = {}
        for attr in after.split(", "):
            splt = attr.split(": ")
            dct[splt[0]] = int(splt[1])
        sues.append(dct)

for i, sue in enumerate(sues):
    for k in sue:
        if ticker[k] != sue[k]:
            break
    else:
        print(i + 1)
