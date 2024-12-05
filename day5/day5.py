

# filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

lines = None
with open(filename, "r") as f:
    lines = f.readlines()

ans = 0
rules = set()
updates = []
second_part = False

for line in lines:
    if line == "\n":
        second_part = True
        continue
    if second_part:
        updates.append(line.strip().split(","))
    else:
        tokens = line.strip().split("|")
        rules.add((tokens[0], tokens[1]))


for upd in updates:
    needs_fix = True
    ordered_upd = []
    i = 0
    while i < len(upd):
        j = i+1
        in_order = True
        while j < len(upd):
            if (upd[j], upd[i]) in rules:
                in_order = False
                needs_fix = False
                upd[j], upd[i] = upd[i], upd[j]
                i -= 1
                break
            j += 1
        if in_order:
            ordered_upd.append(upd[i])
        i += 1

    if not needs_fix:
        ans += int(ordered_upd[len(ordered_upd)//2])


print(ans)
