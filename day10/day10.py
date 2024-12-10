

filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

grid = dict()
potential_trailheads = set()
with open(filename, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            if c == "0":
                potential_trailheads.add((j,i))
            grid[(j,i)] = int(c)

ans = 0

# for thead in potential_trailheads:
#     cur_nodes = set()
#     cur_nodes.add(thead)
#     peaks = set()
#     while len(cur_nodes) > 0:
#         cur = cur_nodes.pop()
#         for adj in [(cur[0]+1, cur[1]), (cur[0], cur[1]+1), (cur[0]-1, cur[1]), (cur[0], cur[1]-1)]:
#             if adj not in grid:
#                 continue
#             if grid[adj] == grid[cur] + 1:
#                 if grid[adj] == 9:
#                     peaks.add(adj)
#                 else:
#                     cur_nodes.add(adj)
#     ans += len(peaks)

def partial_rating(cur):
    """Finds the rating starting from the current location"""
    rating = 0 
    for adj in [(cur[0]+1, cur[1]), (cur[0], cur[1]+1), (cur[0]-1, cur[1]), (cur[0], cur[1]-1)]:
        if adj not in grid:
            continue
        if grid[adj] == grid[cur] + 1:
            if grid[adj] == 9:
                rating += 1
            rating += partial_rating(adj)
    return rating

        
for thead in potential_trailheads:
    rating = partial_rating(thead)
    ans += rating


print(ans)
