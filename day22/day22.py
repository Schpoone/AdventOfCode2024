from collections import Counter

# filename = "example1.txt"
filename = "example2.txt"
filename = "input.txt"

nums = list()
with open(filename, "r") as f:
    lines = f.readlines()
    nums = list(map(lambda line: int(line.strip()),lines))

ans = 0

def mix(secret, other):
    return secret ^ other

def prune(secret):
    return secret % 16777216

def next_secret(secret):
    other = secret * 64
    secret = mix(secret, other)
    secret = prune(secret)

    other = secret // 32
    secret = mix(secret, other)
    secret = prune(secret)

    other = secret * 2048
    secret = mix(secret, other)
    secret = prune(secret)

    return secret

iterations = 2000
# for num in nums:
#     for _ in range(iterations):
#         num = next_secret(num)
#
#     ans += num

changes_to_price_map = Counter()
for num in nums:
    changes = []
    prices = []
    prices.append(int(str(num)[-1]))
    for _ in range(iterations):
        old_price = int(str(num)[-1])
        num = next_secret(num)
        new_price = int(str(num)[-1])
        prices.append(new_price)
        changes.append(new_price-old_price)

    map_for_this_num = Counter()
    for idx in range(4, len(prices)):
        window = tuple(changes[idx-4:idx])
        price = prices[idx]
        if window in map_for_this_num:
            continue
        map_for_this_num[window] += price

    for seq, price in map_for_this_num.items():
        changes_to_price_map[seq] += price

print(max(changes_to_price_map.values()))
