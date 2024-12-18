filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

reg_A = 0
reg_B = 0
reg_C = 0
program = list()
with open(filename, "r") as f:
    lines = f.readlines()
    line_a, line_b, line_c, line_program = lines[0], lines[1], lines[2], lines[4]
    reg_A = int(line_a.split(":")[1].strip())
    reg_B = int(line_b.split(":")[1].strip())
    reg_C = int(line_c.split(":")[1].strip())
    program = [int(num.strip()) for num in line_program.split(":")[1].split(",")]


def combo_operand(num):
    if num in [0, 1, 2, 3]:
        return num
    match num:
        case 4:
            return reg_A
        case 5:
            return reg_B
        case 6:
            return reg_C
    assert num != 7
    return 7


ip = 0

# output = list()
# while ip < len(program) - 1:
#     opcode = program[ip]
#     operand = program[ip+1]
#     match opcode:
#         case 0:
#             reg_A = reg_A // (2**combo_operand(operand))
#         case 1:
#             reg_B = reg_B ^ operand
#         case 2:
#             reg_B = combo_operand(operand) % 8
#         case 3:
#             if reg_A != 0:
#                 ip = operand
#                 continue
#         case 4:
#             reg_B = reg_B ^ reg_C
#         case 5:
#             output.append(str(combo_operand(operand) % 8))
#         case 6:
#             reg_B = reg_A // (2**combo_operand(operand))
#         case 7:
#             reg_C = reg_A // (2**combo_operand(operand))
#
#     ip += 2
#
# print(",".join(output))

program.reverse()


def recurrence_equation(a):
    return ((a % 8) ^ 4 ^ (a >> (a % 8 ^ 1))) % 8

possibilities = [0]
for output in program:
    new_possibilities = list()
    for a in possibilities:
        for i in range(8):
            test = (a<<3) + i
            if recurrence_equation(test) == int(output):
                new_possibilities.append(test)
    possibilities = new_possibilities

print(min(possibilities))
