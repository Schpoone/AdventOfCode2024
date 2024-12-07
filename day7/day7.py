filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

lines = None
with open(filename, "r") as f:
    lines = f.readlines()

ans = 0


def recursive_test_nums(test, cur, nums):
    if len(nums) == 0:
        return test == cur
    return (
        recursive_test_nums(test, cur + nums[0], nums[1:])
        or recursive_test_nums(test, cur * nums[0], nums[1:])
        or recursive_test_nums(test, int(str(cur) + str(nums[0])), nums[1:])
    )


for line in lines:
    sections = line.split(":")
    test = int(sections[0])
    nums = list(map(int, sections[1].split()))
    if recursive_test_nums(test, nums[0], nums[1:]):
        ans += test


print(ans)
