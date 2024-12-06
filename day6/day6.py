

# filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

grid = dict()
with open(filename, "r") as f:
    lines = f.readlines()


height = len(lines)
width = len(lines[0].strip())
pos = (0,0)
dir = "^"
for i, line in enumerate(lines):
    line = line.strip()
    for j, c in enumerate(line):
        grid[(j,i)] = c
        if c == "^":
            pos = (j,i)


def forms_loop(grid, start, start_dir):
    visited = dict()
    just_turned = False
    pos = start
    dir = start_dir
    visited[pos] = dir

    while True:
        match dir:
            case "^":
                new_pos = (pos[0], pos[1]-1)
                if new_pos not in grid:
                    return False
                if grid[new_pos] == "#":
                    dir = ">"
                    just_turned = True
                else:
                    pos = new_pos
                    just_turned = False
            case ">":
                new_pos = (pos[0]+1, pos[1])
                if new_pos not in grid:
                    return False
                if grid[new_pos] == "#":
                    dir = "v"
                    just_turned = True
                else:
                    pos = new_pos
                    just_turned = False
            case "<":
                new_pos = (pos[0]-1, pos[1])
                if new_pos not in grid:
                    return False
                if grid[new_pos] == "#":
                    dir = "^"
                    just_turned = True
                else:
                    pos = new_pos
                    just_turned = False
            case "v":
                new_pos = (pos[0], pos[1]+1)
                if new_pos not in grid:
                    return False
                if grid[new_pos] == "#":
                    dir = "<"
                    just_turned = True
                else:
                    pos = new_pos
                    just_turned = False
        if not just_turned:
            if (pos, dir) in visited.items():
                # for i in range(height):
                #     for j in range(width):
                #         if (j,i) in visited:
                #             print(visited[(j,i)], end="")
                #         else:
                #             print(grid[(j,i)], end="")
                #     print()
                return True
            visited[pos] = dir
            

ans = 0
for i in range(height):
    for j in range(width):
        print((j,i))
        if grid[(j,i)] == ".":
            new_grid = {k: v for k,v in grid.items()}
            new_grid[(j,i)] = "#"
            if forms_loop(new_grid, pos,dir):
                ans += 1

print(ans)
