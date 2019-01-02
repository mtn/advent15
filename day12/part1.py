#!/usr/bin/env python3

import re

with open("input.txt") as f:
    print(sum(map(int, re.findall("-?[0-9]+", f.read()))))
