import functools

filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

patterns = set()
designs = list()
with open(filename, "r") as f:
    sections = f.read().split("\n\n")
    patterns = patterns.union(set(sections[0].split(", ")))
    designs = sections[1].split()

ans = 0

# for design in designs:
#     possibilities = set([""])
#     while len(possibilities) > 0:
#         cur = possibilities.pop()
#         cursor = len(cur)
#         if cursor == len(design):
#             ans += 1
#             break
#         for pattern in patterns:
#             if cursor + len(pattern) > len(design):
#                 continue
#             if all(design[cursor+i] == pattern[i] for i in range(len(pattern))):
#                 possibilities.add(cur+pattern)

# print(ans)

@functools.lru_cache(maxsize=1000000)
def count_possible(s):
    """Count the number of ways the patterns can construct the given string s"""
    ret = 0
    for pattern in patterns:
        if len(pattern) > len(s):
            continue
        if all(s[i] == pattern[i] for i in range(len(pattern))):
            if len(pattern) == len(s):
                ret += 1
            ret += count_possible(s[len(pattern):])
    return ret

for i,s in enumerate(designs):
    print(i,s)
    ans += count_possible(s)

print(ans)
