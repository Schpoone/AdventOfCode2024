filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

computers = set()
connections = dict()
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        tokens = line.strip().split("-")
        computers.add(tokens[0])
        computers.add(tokens[1])
        if tokens[0] not in connections:
            connections[tokens[0]] = []
        connections[tokens[0]].append(tokens[1])
        if tokens[1] not in connections:
            connections[tokens[1]] = []
        connections[tokens[1]].append(tokens[0])

ans = 0

# t_computers = set(filter(lambda c: c[0] == "t", computers))
#
# t_neighbors = dict()
# for c in t_computers:
#     t_neighbors[c] = connections[c]
#
#
# valid_cliques = []
# for t, neighbors in t_neighbors.items():
#     for n in neighbors:
#         neighbors2 = connections[n]
#         for n2 in neighbors2:
#             if n2 in neighbors and n2 != n:
#                 if set([n2, n, t]) not in valid_cliques:
#                     ans += 1
#                     valid_cliques.append(set([n2, n, t]))


def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(set(graph[v])),
            X.intersection(set(graph[v])),
            graph,
        )
        X.add(v)


cliques = list(bron_kerbosch(set(), set(computers), set(), connections))
lan_party = list(max(cliques, key=len))
lan_party.sort()

print(",".join(lan_party))
