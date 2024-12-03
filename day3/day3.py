# any parser or regex probably does this problem really easily

# filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

line = None
with open(filename, "r") as f:
    line = str(f.read())

i = 0
enabled = True

def parse_mul():
    global i
    if line[i:i+4] != "mul(":
        i += 1
        return 0
    i += 4
    j = i + 1
    while j < len(line) and line[i:j].isdigit():
        j += 1
    a = line[i:j-1]
    i = j - 1
    if len(a) == 0:
        return 0
    if line[i] != ',':
        return 0
    i += 1
    j = i + 1
    while j < len(line) and line[i:j].isdigit():
        j += 1
    b = line[i:j-1]
    i = j - 1
    if len(b) == 0:
        return 0
    if line[i] != ')':
        return 0

    i += 1

    return int(a) * int(b)

def parse_do():
    global i, enabled
    if line[i:i+4] == "do()":
        enabled = True
        i += 4

def parse_dont():
    global i, enabled
    if line[i:i+7] == "don't()":
        enabled = False
        i += 7

ans = 0

while i < len(line):
    parse_do()
    parse_dont()
    res = parse_mul()
    if enabled:
        ans += res


print(ans)
