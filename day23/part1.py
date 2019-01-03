#!/usr/bin/env python3

from itertools import combinations

instructions = []
with open("input.txt") as f:
    for line in f:
        op, rest = line[:3], line[4:]
        args = rest.strip().split(",")
        instructions.append((op, args))

ip = 0
registers = { "a": 0, "b": 0 }
while ip < len(instructions) and ip >= 0:
    op, args = instructions[ip]

    if op == "hlf":
        registers[args[0]] //= 2
    elif op == "tpl":
        registers[args[0]] *= 3
    elif op == "inc":
        registers[args[0]] += 1
    elif op == "jmp":
        ip += int(args[0])
        continue
    elif op == "jie":
        reg = args[0]
        offset = int(args[1])
        if registers[reg] % 2 == 0:
            ip += offset
            continue
    elif op == "jio":
        reg = args[0]
        offset = int(args[1])
        if registers[reg] == 1:
            ip += offset
            continue

    ip += 1

print(registers["b"])
