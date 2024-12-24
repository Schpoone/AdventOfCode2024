filename = "example1.txt"
# filename = "example2.txt"
filename = "input.txt"

wires = dict()
gates = list()
with open(filename, "r") as f:
    s1, s2 = f.read().split("\n\n")
    for line in s1.split("\n"):
        wire, value = line.strip().split(": ")
        wires[wire] = int(value)
    for line in s2.strip().split("\n"):
        tokens = line.strip().split()
        gates.append((tokens[0], tokens[1], tokens[2], tokens[4]))

ans = 0


# Part 1: Run this with the initial wires and gates and decode z with the code way below
def process(wires, gates):
    new_wires = dict((k, v) for k, v in wires.items())
    processed = set()
    while len(processed) != len(gates):
        for gate in gates:
            if gate in processed:
                continue
            i1, op, i2, out = gate
            if i1 not in wires or i2 not in wires:
                continue
            processed.add(gate)
            match op:
                case "AND":
                    new_wires[out] = wires[i1] & wires[i2]
                case "OR":
                    new_wires[out] = wires[i1] | wires[i2]
                case "XOR":
                    new_wires[out] = wires[i1] ^ wires[i2]

    return new_wires


x_wires = dict(
    filter(lambda wire_value_pair: wire_value_pair[0][0] == "x", wires.items())
)
# x_bits = ["0"] * len(x_wires)
# for wire, value in x_wires.items():
#     x_bits[len(x_wires) - int(wire[1:]) - 1] = str(value)
# x_str = "".join(x_bits)
# x = int(x_str, 2)

y_wires = dict(
    filter(lambda wire_value_pair: wire_value_pair[0][0] == "y", wires.items())
)
# y_bits = ["0"] * len(y_wires)
# for wire, value in y_wires.items():
#     y_bits[len(y_wires) - int(wire[1:]) - 1] = str(value)
# y_str = "".join(y_bits)
# y = int(y_str, 2)
#
# target_z = x + y
#
# z_wires = dict(
#     filter(lambda wire_value_pair: wire_value_pair[0][0] == "z", wires.items())
# )
# z_bits = ["0"] * len(z_wires)
# for wire, value in z_wires.items():
#     z_bits[len(z_wires) - int(wire[1:]) - 1] = str(value)
# z_str = "".join(z_bits)
# z = int(z_str, 2)

# Part 2 EXPLANATION:
# I assumed the gates would form a standard chain of full adders (with a half adder for bit 0).
# With that assumption, I tried to go through the gates and inspect inputs and outputs.
# For each of those, I tried to save any wires that connected between gates that didn't
# make sense.
# That narrows down the inconsistent inputs and outputs to a reasonable set.
# Then I inspected the input by hand to figure out which outputs are swapped.


# map of wires to what gate they become the input for
wire_to_gate = dict()
for gate in gates:
    i1, op, i2, out = gate
    if i1 not in wire_to_gate:
        wire_to_gate[i1] = []
    if i2 not in wire_to_gate:
        wire_to_gate[i2] = []
    wire_to_gate[i1].append(op)
    wire_to_gate[i2].append(op)

# map of wires to what gate they were the output of
output_wire_to_gate = dict()
for gate in gates:
    i1, op, i2, out = gate
    output_wire_to_gate[out] = op

inconsistent_outputs = set()
inconsistent_inputs = set()
for gate in gates:
    i1, op, i2, out = gate
    if out not in wire_to_gate:
        continue
    match op:
        case "AND":
            if wire_to_gate[out] != ["OR"]:
                inconsistent_outputs.add(out)
            if (
                i1[0] not in "xy"
                and output_wire_to_gate[i1] != "XOR"
                and output_wire_to_gate[i1] != "OR"
            ):
                inconsistent_inputs.add(i1)
            if (
                i2[0] not in "xy"
                and output_wire_to_gate[i2] != "XOR"
                and output_wire_to_gate[i2] != "OR"
            ):
                inconsistent_inputs.add(i2)
        case "OR":
            if not (
                len(wire_to_gate[out]) == 2 and set(wire_to_gate[out]) == {"XOR", "AND"}
            ):
                inconsistent_outputs.add(out)
            if output_wire_to_gate[i1] != "AND":
                inconsistent_inputs.add(i1)
            if output_wire_to_gate[i2] != "AND":
                inconsistent_inputs.add(i2)
        case "XOR":
            if i1[0] not in "xy" and out[0] != "z":
                inconsistent_outputs.add(out)
                inconsistent_inputs.add(i1)
                inconsistent_inputs.add(i2)
            if not (
                len(wire_to_gate[out]) == 2 and set(wire_to_gate[out]) == {"XOR", "AND"}
            ):
                inconsistent_outputs.add(out)
            if i1[0] in "xy" and i2[0] in "xy":
                continue
            if output_wire_to_gate[i1] != "XOR" and output_wire_to_gate[i1] != "OR":
                inconsistent_inputs.add(i1)
            if output_wire_to_gate[i2] != "XOR" and output_wire_to_gate[i2] != "OR":
                inconsistent_inputs.add(i2)

print("inconsistent outputs:", inconsistent_outputs)
print("inconsistent inputs:", inconsistent_inputs)
