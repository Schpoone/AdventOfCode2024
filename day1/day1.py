from collections import Counter

# filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

lines = None
with open(filename, "r") as f:
    lines = f.readlines()

left = []
right = []
for line in lines:
    tokens = line.split()
    left.append(int(tokens[0]))
    right.append(int(tokens[1]))

ctr = Counter(right)
print(ctr)
# left.sort()
# right.sort()

total = 0
# for a, b in zip(left, right):
#     total += abs(a-b)
#

for l in left:
    total += (ctr.get(l) or 0) * l

print(total)
