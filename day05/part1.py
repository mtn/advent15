#!/usr/bin/env python3


nice = 0
with open("input.txt") as f:
    for line in f:
        word = line.strip()
        three_vowels = len([l for l in word if l in "aeiou"]) >= 3

        double_letter = False
        for c, cc in zip(word, word[1:]):
            if c == cc:
                double_letter = True

        if "ab" in word or "cd" in word or "pq" in word or "xy" in word:
            continue

        if double_letter and three_vowels:
            nice += 1

print(nice)
