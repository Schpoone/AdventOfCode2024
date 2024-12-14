import re
import os
import time
import math
from collections import Counter

filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

lines = None
robots = list()
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        m = re.search(r"p=(\d+),(\d+) v=(-*\d+),(-*\d+)", line.strip())
        if m:
            robots.append(
                ((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4))))
            )

# bounds = (11, 7)
bounds = (101, 103)

def print_grid(positions):
    # os.system("clear")
    positions = Counter(positions)
    for i in range(bounds[0]):
        for j in range(bounds[1]):
            if (j,i) in positions:
                print(positions[(j,i)], end="")
            else:
                print(".", end="")
        print(flush=True)


ans = 0
# time = 100
# final_positions = list()

# for robot in robots:
#     p, v = robot
    # final_positions.append(((p[0] + v[0] * time) % bounds[0], (p[1] + v[1] * time) % bounds[1]))

# quad1 = list(filter(lambda p: p[0] < bounds[0]//2 and p[1] < bounds[1]//2, final_positions))
# quad2 = list(filter(lambda p: p[0] > bounds[0]//2 and p[1] < bounds[1]//2, final_positions))
# quad3 = list(filter(lambda p: p[0] < bounds[0]//2 and p[1] > bounds[1]//2, final_positions))
# quad4 = list(filter(lambda p: p[0] > bounds[0]//2 and p[1] > bounds[1]//2, final_positions))
#
# print(len(quad1) * len(quad2) * len(quad3) * len(quad4))

positions = [robot[0] for robot in robots]
print_grid(positions)
states = list()
for i in range(10403):
    print(i, "~" * bounds[0])
    new_positions = list()
    for p, robot in zip(positions, robots):
        v = robot[1]
        new_positions.append(((p[0] + v[0]) % bounds[0], (p[1] + v[1]) % bounds[1]))

    positions = new_positions
    if positions in states:
        break
    states.append(positions)
    if 7000 < i < 9000: # I definitely cheated, but this problem deserved it
        time.sleep(0.2)
        print_grid(positions)
    if i > 9000:
        break

# cycle_time = list()
# for robot in robots:
#     positions = set()
#     p, v = robot
#     i = 0
#     while p not in positions:
#         positions.add(p)
#         new_p = ((p[0]+v[0]) % bounds[0], (p[1]+v[1]) % bounds[1])
#         p = new_p
#         i += 1
#     cycle_time.append(i)
#
# print(math.lcm(*cycle_time))
