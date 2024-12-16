import sys
filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

sys.setrecursionlimit(10000)

lines = None
grid = dict()
start = (0, 0)
with open(filename, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        for j, c in enumerate(line):
            grid[(j, i)] = c
            if c == "S":
                start = (j, i)


# seen: dict[tuple[tuple[int, int], tuple[int, int]], int] = dict()
# cur: dict[tuple[tuple[int, int], tuple[int, int]], int] = dict()
# cur[(start, (1, 0))] = 0
# min_final = None
# while len(cur) > 0:
#     (pos, dir), points = cur.popitem()
#     if grid[pos] == "E":
#         if min_final is None or points < min_final:
#             min_final = points
#         continue
#     next = dict()
#     forward = (pos[0] + dir[0], pos[1] + dir[1])
#     if grid[forward] in ".E":
#         next[(forward, dir)] = points + 1
#     match dir:
#         case (1, 0):
#             next[(pos, (0, 1))] = points + 1000
#             next[(pos, (0, -1))] = points + 1000
#         case (-1, 0):
#             next[(pos, (0, 1))] = points + 1000
#             next[(pos, (0, -1))] = points + 1000
#         case (0, 1):
#             next[(pos, (1, 0))] = points + 1000
#             next[(pos, (-1, 0))] = points + 1000
#         case (0, -1):
#             next[(pos, (1, 0))] = points + 1000
#             next[(pos, (-1, 0))] = points + 1000
#
#     for next_state, next_points in next.items():
#         if next_state not in seen or seen[next_state] > next_points:
#             seen[next_state] = next_points
#             cur[next_state] = next_points
#
# print(min_final)

def recurse(pos, dir, points, seen):
    if grid[pos] == "E":
        if points == 94444:
            return set([pos])
        else:
            return set()
    if (pos, dir) in seen and seen[(pos, dir)] < points:
        return set()
    seen[(pos, dir)] = points
    forward = (pos[0] + dir[0], pos[1] + dir[1])
    next = dict()
    if grid[forward] in ".E":
        next[(forward, dir)] = points + 1
    match dir:
        case (1, 0):
            next[(pos, (0, 1))] = points + 1000
            next[(pos, (0, -1))] = points + 1000
        case (-1, 0):
            next[(pos, (0, 1))] = points + 1000
            next[(pos, (0, -1))] = points + 1000
        case (0, 1):
            next[(pos, (1, 0))] = points + 1000
            next[(pos, (-1, 0))] = points + 1000
        case (0, -1):
            next[(pos, (1, 0))] = points + 1000
            next[(pos, (-1, 0))] = points + 1000

    tiles = set()
    for next_state, next_points in next.items():
        recursed_tiles = recurse(next_state[0], next_state[1], next_points, seen)
        tiles = tiles.union(recursed_tiles)
    if len(tiles) > 0:
        tiles.add(pos)

    return tiles

print(len(recurse(start, (1,0), 0, dict())))
