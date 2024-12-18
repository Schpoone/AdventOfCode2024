filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

lines = None
# width, height = 7, 7
width, height = 71, 71
coords = list()
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        tokens = line.strip().split(",")
        coords.append((int(tokens[0]), int(tokens[1])))

# print(coords)
ans = 0

# obstacles = set(coords[:12])
obstacles = set(coords[:1024])


def in_grid(coord):
    x, y = coord
    return x >= 0 and y >= 0 and x < width and y < height

# dist to end
def dist(coord):
    return width-1-coord[0] + height-1-coord[1]

def astar():
    open_list = dict()
    closed_list = set()
    open_list[(0,0)] = 0
    while len(open_list) > 0:
        coord, g = min(open_list.items(), key=lambda x: x[1] + dist(x[0]))
        open_list.pop(coord)
        closed_list.add(coord)

        if coord == (width - 1, height - 1):
            return g

        x,y = coord
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            adj = (x + dx, y + dy)
            if not in_grid(adj) or adj in obstacles:
                continue
            if adj in closed_list:
                continue
            if adj in open_list and open_list[adj] < g + 1:
                continue
            open_list[adj] = g + 1

print(astar())

for c in coords:
    obstacles.add(c)
    print(c)
    print(astar())
