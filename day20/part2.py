#!/usr/bin/env python3

# super super slow

from collections import defaultdict
from itertools import count

inp = 33100000

from functools import reduce

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def num_presents(n):
    fact = factors(n)
    presents = 0
    for f in fact:
        if n // f <= 50:
            presents += 11 * f
    return presents

for i in count(1):
    n = num_presents(i)
    if num_presents(i) >= inp:
        print(i)
        break
