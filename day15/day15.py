filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

grid = dict()
height = 0
width = 0
moves = None
pos = (0, 0)
with open(filename, "r") as f:
    parts = f.read().split("\n\n")
    height = len(parts[0].splitlines())
    width = len(parts[0].splitlines()[0].strip())
    for i, line in enumerate(parts[0].splitlines()):
        for j, c in enumerate(line):
            # if c == "@":
            #     pos = (j, i)
            # grid[(j, i)] = c
            actual_pos = (2 * j, i)
            match c:
                case "#":
                    grid[actual_pos] = "#"
                    grid[(actual_pos[0] + 1, actual_pos[1])] = "#"
                case "O":
                    grid[actual_pos] = "["
                    grid[(actual_pos[0] + 1, actual_pos[1])] = "]"
                case ".":
                    grid[actual_pos] = "."
                    grid[(actual_pos[0] + 1, actual_pos[1])] = "."
                case "@":
                    grid[actual_pos] = "@"
                    grid[(actual_pos[0] + 1, actual_pos[1])] = "."
                    pos = actual_pos

    moves = "".join(parts[1].splitlines())

width *= 2


def print_grid(grid):
    for i in range(height):
        for j in range(width):
            print(grid[(j, i)], end="")
        print()


ans = 0

for move in moves:
    # print(pos, move)
    # print_grid(grid)
    dir = (0, 0)
    match move:
        case "<":
            dir = (-1, 0)
        case ">":
            dir = (1, 0)
        case "^":
            dir = (0, -1)
        case "v":
            dir = (0, 1)
    # boxes_to_move = list()
    boxes_to_move = dict()
    # p = (pos[0] + dir[0], pos[1] + dir[1])
    # while grid[p] == "O":
    #     boxes_to_move.append(p)
    #     p = (p[0] + dir[0], p[1] + dir[1])
    tiles_to_check = set([(pos[0] + dir[0], pos[1] + dir[1])])
    hit_wall = False
    while len(tiles_to_check) > 0:
        tile = tiles_to_check.pop()
        if grid[tile] == "#":
            hit_wall = True
            break
        if grid[tile] == ".":
            continue
        assert grid[tile] in "[]"
        other_half = tile
        if grid[tile] == "[":
            other_half = (tile[0] + 1, tile[1])
        if grid[tile] == "]":
            other_half = (tile[0] - 1, tile[1])
        boxes_to_move[tile] = grid[tile]
        boxes_to_move[other_half] = grid[other_half]
        tiles_affected = [(p[0] + dir[0], p[1] + dir[1]) for p in [tile, other_half]]
        tiles_to_check = tiles_to_check.union(
            set(tile for tile in tiles_affected if tile not in boxes_to_move)
        )
    # if grid[p] == "#":
    #     continue
    if hit_wall:
        continue
    # assert grid[p] == "."
    # for box in boxes_to_move:
    #     grid[(box[0] + dir[0], box[1] + dir[1])] = "O"
    for box in boxes_to_move:
        grid[box] = "."
    for box, c in boxes_to_move.items():
        grid[(box[0] + dir[0], box[1] + dir[1])] = c
    grid[pos] = "."
    pos = (pos[0] + dir[0], pos[1] + dir[1])
    grid[pos] = "@"

for i in range(height):
    for j in range(width):
        # if grid[(j, i)] == "O":
        if grid[(j, i)] == "[":
            ans += 100 * i + j


print(ans)
