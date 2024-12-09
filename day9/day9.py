filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

line = None
with open(filename, "r") as f:
    line = f.read().strip()

id = 0

disk = list()
filesizes = list()
file_positions = list()
cur_block = 0

for idx, size in enumerate(line):
    if idx % 2 == 0:
        for _ in range(int(size)):
            disk.append(str(id))
        filesizes.append(int(size))
        file_positions.append(cur_block)
        id += 1
    else:
        for _ in range(int(size)):
            disk.append(".")
    cur_block += int(size)

filesizes.reverse()
file_positions.reverse()


ans = 0
# i = 0
# j = len(disk) - 1
#
# while i < j:
#     while disk[i] != ".":
#         i += 1
#     while disk[j] == ".":
#         j -= 1
#     if i >= j:
#         break
#     disk[i], disk[j] = disk[j], disk[i]

id = len(filesizes) - 1
for filesize, file_pos in zip(filesizes, file_positions):
    print(id)
    # print("".join(disk))
    leftmost_gap = (len(disk), 0) # idx, size
    cur_gap_size = 0
    for idx, c in enumerate(disk):
        if idx > file_pos:
            break
        if c != ".":
            if cur_gap_size >= filesize and idx - cur_gap_size < leftmost_gap[0]:
                leftmost_gap = (idx - cur_gap_size, cur_gap_size)
            cur_gap_size = 0
        else:
            cur_gap_size += 1
    if leftmost_gap == (len(disk), 0):
        id -= 1
        continue

    disk[leftmost_gap[0]:leftmost_gap[0]+leftmost_gap[1]] = filesize * [str(id)] + (leftmost_gap[1]-filesize) * ["."]
    disk[file_pos:file_pos+filesize] = filesize * "."


    id -= 1

print(disk)


for idx, c in enumerate(disk):
    if c != ".":
        ans += idx * int(c)


print(ans)
