# filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

text = None
with open(filename, "r") as f:
    text = f.read()

ans = 0
grid: dict[tuple[int, int], str] = {}
# x_locs: list[tuple[int, int]] = []
a_locs = []

i = 0
j = 0
for c in text:
    if c == "\n":
        i = 0
        j += 1
        continue
    grid[(i, j)] = c
    # if c == "X":
    #     x_locs.append((i, j))
    if c == "A":
        a_locs.append((i, j))
    i += 1

# for x_loc in x_locs:
#     if (
#         (x_loc[0] + 3, x_loc[1]) in grid
#         and grid[(x_loc[0] + 1, x_loc[1])] == "M"
#         and grid[(x_loc[0] + 2, x_loc[1])] == "A"
#         and grid[(x_loc[0] + 3, x_loc[1])] == "S"
#     ):
#         ans += 1
#     if (
#         (x_loc[0] + 3, x_loc[1] + 3) in grid
#         and grid[(x_loc[0] + 1, x_loc[1] + 1)] == "M"
#         and grid[(x_loc[0] + 2, x_loc[1] + 2)] == "A"
#         and grid[(x_loc[0] + 3, x_loc[1] + 3)] == "S"
#     ):
#         ans += 1
#     if (
#         (x_loc[0], x_loc[1] + 3) in grid
#         and grid[(x_loc[0], x_loc[1] + 1)] == "M"
#         and grid[(x_loc[0], x_loc[1] + 2)] == "A"
#         and grid[(x_loc[0], x_loc[1] + 3)] == "S"
#     ):
#         ans += 1
#     if (
#         (x_loc[0] - 3, x_loc[1] + 3) in grid
#         and grid[(x_loc[0] - 1, x_loc[1] + 1)] == "M"
#         and grid[(x_loc[0] - 2, x_loc[1] + 2)] == "A"
#         and grid[(x_loc[0] - 3, x_loc[1] + 3)] == "S"
#     ):
#         ans += 1
#     if (
#         (x_loc[0] - 3, x_loc[1]) in grid
#         and grid[(x_loc[0] - 1, x_loc[1])] == "M"
#         and grid[(x_loc[0] - 2, x_loc[1])] == "A"
#         and grid[(x_loc[0] - 3, x_loc[1])] == "S"
#     ):
#         ans += 1
#     if (
#         (x_loc[0] - 3, x_loc[1] - 3) in grid
#         and grid[(x_loc[0] - 1, x_loc[1] - 1)] == "M"
#         and grid[(x_loc[0] - 2, x_loc[1] - 2)] == "A"
#         and grid[(x_loc[0] - 3, x_loc[1] - 3)] == "S"
#     ):
#         ans += 1
#     if (
#         (x_loc[0], x_loc[1] - 3) in grid
#         and grid[(x_loc[0], x_loc[1] - 1)] == "M"
#         and grid[(x_loc[0], x_loc[1] - 2)] == "A"
#         and grid[(x_loc[0], x_loc[1] - 3)] == "S"
#     ):
#         ans += 1
#     if (
#         (x_loc[0] + 3, x_loc[1] - 3) in grid
#         and grid[(x_loc[0] + 1, x_loc[1] - 1)] == "M"
#         and grid[(x_loc[0] + 2, x_loc[1] - 2)] == "A"
#         and grid[(x_loc[0] + 3, x_loc[1] - 3)] == "S"
#     ):
#         ans += 1

for a_loc in a_locs:
    surrounding_coords = [
        (a_loc[0] + 1, a_loc[1] + 1),
        (a_loc[0] + 1, a_loc[1] - 1),
        (a_loc[0] - 1, a_loc[1] - 1),
        (a_loc[0] - 1, a_loc[1] + 1),
    ]
    surrounding_chars = [
        grid[coord] if coord in grid else None for coord in surrounding_coords
    ]
    print(surrounding_chars)
    if (
        surrounding_chars == ["M", "M", "S", "S"]
        or surrounding_chars == ["S", "S", "M", "M"]
        or surrounding_chars == ["M", "S", "S", "M"]
        or surrounding_chars == ["S", "M", "M", "S"]
    ):

        ans += 1

print(ans)
