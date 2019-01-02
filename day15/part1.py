#!/usr/bin/env python3

import re

ingredients = []
with open("input.txt") as f:
    for line in f:
        attrs = capacity, durability, flavor, texture, calories = list(map(int, re.findall("-?[0-9]", line)))
        name = line.split()[0][:-1].lower()
        ingredients.append(attrs)

max_score = -1
for sugar in range(0, 101):
    for sprinkles in range(0, 101 - sugar):
        for candy in range(0, 101 - sugar - sprinkles):
            chocolate = 100 - sugar - sprinkles - candy

            nums = [sugar, sprinkles, candy, chocolate]
            capacity = max(0, sum([x * y for x, y in zip([i[0] for i in ingredients], nums)]))
            durability = max(0, sum([x * y for x, y in zip([i[1] for i in ingredients], nums)]))
            flavor = max(0, sum([x * y for x, y in zip([i[2] for i in ingredients], nums)]))
            texture = max(0, sum([x * y for x, y in zip([i[3] for i in ingredients], nums)]))

            score = capacity * durability * flavor * texture
            max_score = max(max_score, score)

print(max_score)

