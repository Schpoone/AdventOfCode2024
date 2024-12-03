
filename = "example1.txt"
# filename = "example2.txt"
# filename = "input.txt"

lines = None
with open(filename, "r") as f:
    lines = f.readlines()

# this can be done better by taking the list of differences, mapping them to
# check the cases, and calling all()
def calc_safety(levels):
    levels2 = levels.copy()
    levels2.sort()
    levels3 = levels.copy()
    levels3.sort(reverse=True)
    if levels2 == levels:
        for idx, level in enumerate(levels):
            if idx == 0:
                continue
            diff = level - levels[idx-1]
            if diff < 1 or diff > 3:
                break
        else:
            return True
    elif levels3 == levels:
        for idx, level in enumerate(levels):
            if idx == 0:
                continue
            diff = levels[idx-1] - level
            if diff < 1 or diff > 3:
                break
        else:
            return True
    return False

ans = 0
for line in lines:
    levels = line.split()
    levels = [int(x) for x in levels]
    for idx, _ in enumerate(levels):
        if calc_safety(levels):
            ans += 1
            break
        if calc_safety(levels[:idx] + levels[idx + 1:]):
            ans += 1
            break




print(ans)
