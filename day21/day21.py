import functools
import itertools

filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

numpad_positions = {
    "0": (1, 3),
    "A": (2, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
}

directional_positions = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

codes = list()
with open(filename, "r") as f:
    codes = f.readlines()

ans = 0


@functools.lru_cache(maxsize=100000000)
def iterative_new_directions(directions, iterations):
    if iterations == 0:
        return len(directions)
    forced = set()
    new_directions = []
    for c1, c2 in zip("A" + directions, directions):
        p1, p2 = directional_positions[c1], directional_positions[c2]
        diff = (p2[0] - p1[0], p2[1] - p1[1])
        next_token = ""
        if (p1[0], p2[1]) == (0, 0):
            next_token += ">" * abs(diff[0])
            next_token += "^" * abs(diff[1])
            next_token += "A"
            forced.add(len(new_directions))
            new_directions.append(next_token)
            continue
        if (p2[0], p1[1]) == (0, 0):
            next_token += "v" * abs(diff[1])
            next_token += "<" * abs(diff[0])
            next_token += "A"
            forced.add(len(new_directions))
            new_directions.append(next_token)
            continue
        if diff[0] < 0:
            next_token += "<" * abs(diff[0])
        if diff[1] > 0:
            next_token += "v" * abs(diff[1])
        if diff[1] < 0:
            next_token += "^" * abs(diff[1])
        if diff[0] > 0:
            next_token += ">" * abs(diff[0])
        next_token += "A"
        new_directions.append(next_token)
    ret = 0
    for i, token in enumerate(new_directions):
        if i in forced:
            min_length = iterative_new_directions(token, iterations - 1)
        else:
            possibilities = itertools.permutations(token[:-1])
            min_length = 10000000000000000
            for p in possibilities:
                p = "".join(p)
                length = iterative_new_directions(p + "A", iterations - 1)
                if length < min_length:
                    min_length = length
        ret += min_length

    return ret


for code in codes:
    code = code.strip()
    directions = []
    forced = set()
    for c1, c2 in zip("A" + code, code):
        p1, p2 = numpad_positions[c1], numpad_positions[c2]
        diff = (p2[0] - p1[0], p2[1] - p1[1])
        next_token = ""
        if (p1[0], p2[1]) == (0, 3):
            next_token += ">" * abs(diff[0])
            next_token += "v" * abs(diff[1])
            next_token += "A"
            forced.add(len(directions))
            directions.append(next_token)
            continue
        if (p2[0], p1[1]) == (0, 3):
            next_token += "^" * abs(diff[1])
            next_token += "<" * abs(diff[0])
            next_token += "A"
            forced.add(len(directions))
            directions.append(next_token)
            continue
        if diff[0] < 0:
            next_token += "<" * abs(diff[0])
        if diff[1] > 0:
            next_token += "v" * abs(diff[1])
        if diff[0] > 0:
            next_token += ">" * abs(diff[0])
        if diff[1] < 0:
            next_token += "^" * abs(diff[1])
        next_token += "A"
        directions.append(next_token)

    for i, token in enumerate(directions):
        if i in forced:
            min_length = iterative_new_directions(token, 25)
        else:
            possibilities = itertools.permutations(token[:-1])
            min_length = 10000000000000000
            for p_tuple in possibilities:
                p = "".join(p_tuple)
                length = iterative_new_directions(p + "A", 25)
                if length < min_length:
                    min_length = length

        ans += min_length * int(code[:-1])

print(ans)
