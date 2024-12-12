import random

filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

lines = None
grid = dict()
height = 0
width = 0
plants: dict[str, set[tuple[int, int]]] = dict()
with open(filename, "r") as f:
    lines = f.readlines()
    height = len(lines)
    width = len(lines[0].strip())
    for i, line in enumerate(lines):
        line = line.strip()
        for j, c in enumerate(line):
            grid[(j, i)] = c
            if c in plants:
                plants[c].add((j, i))
            else:
                plants[c] = set([(j, i)])

ans = 0


def visualize_regions(regions):
    color_map = [random.randrange(20, 256) for _ in regions]
    for i in range(height):
        for j in range(width):
            for idx, region in enumerate(regions):
                if (j, i) in region:
                    print(f"\33[38;5;{color_map[idx]}m{grid[(j,i)]}\33[0m", end="")
        print()


all_regions = []

for plant_type, plots in plants.items():
    regions: list[set[tuple[int, int]]] = list()
    unseen = plots.copy()
    while len(unseen) > 0:
        cur_region = set()
        cur = set([unseen.pop()])
        while len(cur) > 0:
            plot = cur.pop()
            unseen.discard(plot)
            if plot in cur_region:
                continue
            cur_region.add(plot)

            adj4 = [
                (plot[0] + 1, plot[1]),
                (plot[0] - 1, plot[1]),
                (plot[0], plot[1] + 1),
                (plot[0], plot[1] - 1),
            ]
            adj4 = list(filter(lambda adj: adj in plots, adj4))
            cur = cur.union(set(adj4))
        regions.append(cur_region)

    all_regions.extend(regions)

    # for region in regions:
    #     perimeter = 0
    #     for plot in region:
    #         adj4 = [(plot[0]+1, plot[1]), (plot[0]-1, plot[1]), (plot[0], plot[1]+1), (plot[0], plot[1]-1)]
    #         for adj in adj4:
    #             if adj not in region:
    #                 perimeter += 1
    #     ans += perimeter * len(region)

    for region in regions:
        area = len(region)
        edges = set()
        for plot in region:
            adj4 = [
                (plot[0] + 1, plot[1]),
                (plot[0] - 1, plot[1]),
                (plot[0], plot[1] + 1),
                (plot[0], plot[1] - 1),
            ]
            edges = edges.union(set([(plot, adj) for adj in adj4 if adj not in region]))

        num_sides = 0
        while len(edges) > 0:
            num_sides += 1
            in_plot, out_plot = edges.pop()
            dir = (
                "h" if out_plot[0] - in_plot[0] == 0 else "v"
            )  # direction of the wall itself
            if dir == "h":
                next_in = (in_plot[0] + 1, in_plot[1])
                next_out = (out_plot[0] + 1, out_plot[1])
                while (next_in, next_out) in edges:
                    edges.discard((next_in, next_out))
                    next_in = (next_in[0] + 1, next_in[1])
                    next_out = (next_out[0] + 1, next_out[1])
                next_in = (in_plot[0] - 1, in_plot[1])
                next_out = (out_plot[0] - 1, out_plot[1])
                while (next_in, next_out) in edges:
                    edges.discard((next_in, next_out))
                    next_in = (next_in[0] - 1, next_in[1])
                    next_out = (next_out[0] - 1, next_out[1])
            else:
                next_in = (in_plot[0], in_plot[1] + 1)
                next_out = (out_plot[0], out_plot[1] + 1)
                while (next_in, next_out) in edges:
                    edges.discard((next_in, next_out))
                    next_in = (next_in[0], next_in[1] + 1)
                    next_out = (next_out[0], next_out[1] + 1)
                next_in = (in_plot[0], in_plot[1] - 1)
                next_out = (out_plot[0], out_plot[1] - 1)
                while (next_in, next_out) in edges:
                    edges.discard((next_in, next_out))
                    next_in = (next_in[0], next_in[1] - 1)
                    next_out = (next_out[0], next_out[1] - 1)

        ans += area * num_sides


visualize_regions(all_regions)


print(ans)
