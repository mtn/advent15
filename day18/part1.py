#!/usr/bin/env python3

grid = []
with open("input.txt") as f:
    for y, line in enumerate(f):
        grid.append([])
        for x, ch in enumerate(line.strip()):
            grid[y].append(ch)

width = len(grid[0])
height = len(grid)
grid[0][0] = grid[height-1][0] = grid[0][width-1] = grid[height-1][width-1] = "#"

def get_neighbors(y, x):
    on_counts = off_counts = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == dx == 0:
                continue
            if x + dx < 0 or x + dx >= width or y + dy < 0 or y + dy >= height:
                continue

            if grid[y+dy][x+dx] == "#":
                on_counts += 1
            else:
                off_counts += 1

    return on_counts, off_counts

def step():
    new_grid = [["." for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            if grid[y][x] == ".":
                num_on, _ = get_neighbors(y, x)
                if num_on == 3:
                    new_grid[y][x] = "#"
            elif grid[y][x] == "#":
                num_on, _ = get_neighbors(y, x)
                if num_on in [2, 3]:
                    new_grid[y][x] = "#"

    new_grid[0][0] = new_grid[height-1][0] = new_grid[0][width-1] = new_grid[height-1][width-1] = "#"

    return new_grid

def print_grid():
    for y in range(height):
        row_str = ""
        for ch in grid[y]:
            row_str += ch
        print(row_str)
    print("")

for i in range(100):
    grid = step()

ans = 0
for y in range(height):
    for x in range(width):
        ans += 1 if grid[y][x] == "#" else 0
print(ans)


