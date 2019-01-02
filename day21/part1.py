#!/usr/bin/env python3

import re
from itertools import combinations, count

class Unit(object):
    def __init__(self, name, hp, arm, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.arm = arm

    def attack(self, target):
        "returns whether or not combat finished"
        assert isinstance(target, Unit)
        dmg = max(1, self.dmg - target.arm)
        target.hp -= dmg
        if target.hp <= 0:
            return True
        return False

    def __repr__(self):
        return f"Unit(hp={self.hp}, arm={self.arm}, dmg={self.dmg})"

with open("input.txt") as f:
    for line in f:
        if "Hit Points:" in line:
            boss_hp = int(re.findall("[0-9]+", line)[0])
        elif "Damage:" in line:
            dmg = int(re.findall("[0-9]+", line)[0])
        elif "Armor:" in line:
            arm = int(re.findall("[0-9]+", line)[0])

boss = Unit("Boss", boss_hp, arm, dmg)

weapons = {
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
}

armor = {
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
}

rings = {
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
}

from copy import deepcopy
player = Unit("player", 100, 0, 0)
costs = []
for w in weapons:
    for a in armor:
        for r in combinations(rings, 2):
            boss.hp = boss_hp
            player.hp = 100

            cost = w[0] + a[0] + sum(r[0] for r in r)
            player.dmg = w[1] + a[1] + sum(r[1] for r in r)
            player.arm = w[2] + a[2] + sum(r[2] for r in r)

            while True:
                if player.attack(boss):
                    costs.append(cost)
                    break
                if boss.attack(player):
                    break

print(min(costs))
