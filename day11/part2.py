#!/usr/bin/env python3

from itertools import groupby
from collections import defaultdict
import re

def increment(word):
    inc_offset = 1

    new_word = [ch for ch in word]
    while new_word[-inc_offset] == "z":
        new_word[-inc_offset] = "a"
        if new_word[-inc_offset - 1] == "z":
            inc_offset += 1
            continue
        else:
            new_word[-inc_offset - 1] = chr(ord(new_word[-inc_offset - 1]) + 1)
            return "".join(new_word)

    new_word[-inc_offset] = chr(ord(new_word[-inc_offset]) + 1)
    return "".join(new_word)

inp = "xx"
inp = increment(inp)
assert inp == "xy"
inp = increment(inp)
assert inp == "xz"
inp = increment(inp)
assert inp == "ya"
inp = increment(inp)
assert inp == "yb"

inp = "hxbxwxba"

def is_good(word):
    increasing_seq = False
    for c, cc, ccc in zip(word, word[1:], word[2:]):
        if ord(c) + 1 == ord(cc) and ord(cc) + 1 == ord(ccc):
            increasing_seq = True

    has_confusing = False
    if "i" in word or "o" in word or "l" in word:
        has_confusing = True

    doubled = not len(re.findall(r'([a-z])\1', word)) < 2

    return doubled and not has_confusing and increasing_seq

assert not is_good("hijklmmn")
assert not is_good("abbceffg")
assert not is_good("abbcegjk")
assert is_good("ghjaabcc")

inp = "hxbxwxba"
while not is_good(inp):
    inp = increment(inp)
inp = increment(inp)
while not is_good(inp):
    inp = increment(inp)

print(inp)
