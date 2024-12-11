import concurrent.futures
from functools import lru_cache

filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

line = None
with open(filename, "r") as f:
    line = f.read().strip().split()
    line = list(map(int, line))

ans = 0

# for i in range(25):
#     new_line = []
#     for stone in line:
#         if stone == 0:
#             new_line.append(1)
#             continue
#         stone_str = str(stone)
#         if len(str(stone)) % 2 == 0:
#             new_line.append(int(stone_str[:len(stone_str)//2]))
#             new_line.append(int(stone_str[len(stone_str)//2:]))
#             continue
#         new_line.append(stone*2024)
#     line = new_line


@lru_cache(maxsize=1024)
def blink(line, num_times):
    if num_times == 0:
        return len(line)
    ret = 0
    for stone in line:
        if stone == 0:
            ret += blink(tuple([1]), num_times - 1)
            continue
        stone_str = str(stone)
        if len(str(stone)) % 2 == 0:
            ret += blink(
                tuple(
                    [
                        int(stone_str[: len(stone_str) // 2]),
                        int(stone_str[len(stone_str) // 2 :]),
                    ]
                ),
                num_times - 1,
            )
            continue
        ret += blink(tuple([stone * 2024]), num_times - 1)
    return ret


num_times = 75

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(blink, tuple([stone]), num_times) for stone in line]
    for future in concurrent.futures.as_completed(futures):
        ans += future.result()


print(ans)
