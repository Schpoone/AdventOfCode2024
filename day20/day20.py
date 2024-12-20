from collections import Counter

filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

start = (0, 0)
end = (0, 0)
walls = set()
with open(filename, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "S":
                start = (j, i)
            elif c == "E":
                end = (j, i)
            elif c == "#":
                walls.add((j, i))

path = []
seen = set()
cur = start
while cur != end:
    path.append(cur)
    seen.add(cur)
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        adj = (cur[0] + dx, cur[1] + dy)
        if adj in seen or adj in walls:
            continue
        cur = adj
        break
path.append(end)

ans = 0

# cheats = Counter()
# for i, start_pos in enumerate(path):
#     for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#         try:
#             end_pos = (start_pos[0] + dx + dx, start_pos[1] + dy + dy)
#             j = path.index(end_pos)
#             cheats[j - i - 2] += 1
#             if j - i - 2 >= 100:
#                 ans += 1
#         except ValueError:
#             continue

path_indexes = dict()
for i, pos in enumerate(path):
    path_indexes[pos] = i


def dist(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])


cheats = Counter()
for i, start_pos in enumerate(path):
    valid_end_positions = set()
    for x in range(start_pos[0] - 20, start_pos[0] + 21):
        for y in range(start_pos[1] - 20, start_pos[1] + 21):
            if (x, y) in path_indexes and dist(start_pos, (x, y)) <= 20:
                valid_end_positions.add((x, y))
    for end_pos in valid_end_positions:
        j = path_indexes[end_pos]
        time_saved = j - i - (dist(start_pos, end_pos))
        if time_saved > 0:
            cheats[time_saved] += 1
        if time_saved >= 100:
            ans += 1

print(cheats)
print(ans)
