#!/usr/bin/env python3

from itertools import groupby

inp = "1113222113"

for i in range(50):
    next_str = "".join(str(len(list(v))) + k for k, v in groupby(inp))
    inp = next_str

print(len(inp))
