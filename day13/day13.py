import re
from scipy.optimize import LinearConstraint, milp, Bounds
import numpy as np

filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

machines: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]] = []
with open(filename, "r") as f:
    input = f.read()
    for machine_txt in input.split("\n\n"):
        lines = machine_txt.splitlines()
        assert len(lines) == 3
        a, b, prize = (0,0), (0,0), (0,0)
        pattern = r"X\+(\d+), Y\+(\d+)"
        m = re.search(pattern, lines[0])
        if m:
            a = (int(m.group(1)), int(m.group(2)))
        m = re.search(pattern, lines[1])
        if m:
            b = (int(m.group(1)), int(m.group(2)))
        pattern = r"X=(\d+), Y=(\d+)"
        m = re.search(pattern, lines[2])
        if m:
            prize = (int(m.group(1)), int(m.group(2)))
        machines.append((a, b, prize))

part2_machines = []
for machine in machines:
    part2_machines.append(
        (
            machine[0],
            machine[1],
            (machine[2][0] + 10000000000000, machine[2][1] + 10000000000000),
        )
    )
machines = part2_machines

ans = 0

# for a, b, prize in machines:
#     print(a, b, prize)
#     min_price = 400
#     found_combo = False
#     for num_a in range(max(prize[0] // a[0], prize[1] // a[1])):
#         num_b = 0
#         position = (num_a * a[0] + num_b * b[0], num_a * a[1] + num_b * b[1])
#         while position[0] <= prize[0] and position[1] <= prize[1]:
#             if position == prize:
#                 found_combo = True
#                 min_price = min(num_a * 3 + num_b, min_price)
#                 break
#             num_b += 1
#             position = (num_a * a[0] + num_b * b[0], num_a * a[1] + num_b * b[1])
#     ans += min_price if found_combo else 0

# Constraints:
#    prize.x <= a.x * num_a + b.x * num_b <= prize.x
#    prize.y <= a.y * num_a + b.y * num_b <= prize.y
#    num_a, num_b >= 100

c = np.array([3, 1])
for a, b, prize in machines:
    print(a, b, prize)
    A = np.array([[a[0], b[0]], [a[1], b[1]]])
    b_u = np.array([prize[0], prize[1]])
    b_l = b_u
    constraints = LinearConstraint(A, lb=b_l, ub=b_u)
    integrality = np.ones_like(c)
    res = milp(c=c, constraints=constraints, integrality=integrality, options={"presolve": False})
    ans += res.fun if res.success else 0

print(ans)
