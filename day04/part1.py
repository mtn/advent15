#!/usr/bin/env python3

import hashlib

inp = "yzbqklnj"
i = 0
while True:
    m = hashlib.md5()
    m.update(str.encode("{}{}".format(inp, i)))

    if m.hexdigest()[:5] == "00000":
        print(i)
        break
    i += 1
