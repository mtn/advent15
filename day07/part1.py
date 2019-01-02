#!/usr/bin/env python3

inputs = {}
reduced = {}
with open("input.txt") as f:
    for line in f:
        inp, to = map(lambda x: x.strip(), line.split("->"))
        inputs[to] = inp.split(" ")

def reduce(name):
    try:
        return int(name)
    except:
        pass

    if name not in reduced:
        exp = inputs[name]
        if len(exp) == 1:
            res = reduce(exp[0])
        else:
            op = exp[-2]
            if op == "NOT":
                res = ~reduce(exp[1]) & 0xffff
            elif op == "AND":
                res = reduce(exp[0]) & reduce(exp[2])
            elif op == "OR":
                res = reduce(exp[0]) | reduce(exp[2])
            elif op == "LSHIFT":
                res = reduce(exp[0]) << reduce(exp[2])
            elif op == "RSHIFT":
                res = reduce(exp[0]) >> reduce(exp[2])
        reduced[name] = res

    return reduced[name]

print(reduce("a"))
