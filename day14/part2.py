#!/usr/bin/env python3

import re

RESTING = 0
RUNNING = 1

class Reindeer(object):
    def __init__(self, spd, spd_time, rst_time):
        self.spd = spd
        self.spd_time = spd_time
        self.rst_time = rst_time

        self.status = RUNNING
        self.remaining = spd_time
        self.travelled = 0
        self.points = 0

    def step(self):
        if self.status == RUNNING:
            self.travelled += self.spd
        if self.remaining == 1:
            if self.status == RUNNING:
                self.status = RESTING
                self.remaining = self.rst_time
                return
            if self.status == RESTING:
                self.status = RUNNING
                self.remaining = self.spd_time
                return
        self.remaining -= 1

reindeer = set()
with open("input.txt") as f:
    for line in f:
        spd, spd_time, rst_time = map(int, re.findall("[0-9]+", line))
        reindeer.add(Reindeer(spd, spd_time, rst_time))
        name = line.split()[0]

for i in range(2503):
    for r in reindeer:
        r.step()
    max_dist = max(map(lambda x: x.travelled, reindeer))
    for r in reindeer:
        if r.travelled == max_dist:
            r.points += 1

print(max(map(lambda x: x.points, reindeer)))
