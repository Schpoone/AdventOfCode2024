import math

# filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

antennas = dict()
height, width = 0, 0
with open(filename, "r") as f:
    lines = f.readlines()
    height = len(lines)
    width = len(lines[0].strip())
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c.isdigit() or c.isalpha():
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append((j,i))

antinodes = set()
# for locs in antennas.values():
#     for i, loc1 in enumerate(locs):
#         j = i + 1
#         while j < len(locs):
#             loc2 = locs[j]
#             antinodes.add((2*loc1[0]-loc2[0], 2*loc1[1]-loc2[1]))
#             antinodes.add((2*loc2[0]-loc1[0], 2*loc2[1]-loc1[1]))
#             j += 1
#
# antinodes = set(filter(lambda node: node[0] >= 0 and node[1] >= 0 and node[0] < width and node[1] < height, antinodes))

for locs in antennas.values():
    for i, loc1 in enumerate(locs):
        j = i + 1
        while j < len(locs):
            loc2 = locs[j]
            slope = (loc2[0] - loc1[0], loc2[1] - loc1[1])
            slope = (slope[0] // math.gcd(*slope), slope[1] // math.gcd(*slope))
            x,y = loc1[0], loc1[1]
            while x >= 0 and y >= 0 and x < width and y < height:
                antinodes.add((x,y))
                x += slope[0]
                y += slope[1]
            x,y = loc1[0], loc1[1]
            while x >= 0 and y >= 0 and x < width and y < height:
                antinodes.add((x,y))
                x -= slope[0]
                y -= slope[1]
            j += 1


print(len(antinodes))
