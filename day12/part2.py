#!/usr/bin/env python3

import json

with open("input.txt") as f:
    inp = json.loads(f.read().strip())

def recursive_sum(inp):
    if isinstance(inp, int):
        return inp

    if isinstance(inp, list):
        return sum([recursive_sum(i) for i in inp])
    if not isinstance(inp, dict):
        return 0
    assert isinstance(inp, dict)
    if "red" in inp.values():
        return 0
    return recursive_sum(list(inp.values()))

print(recursive_sum(inp))
