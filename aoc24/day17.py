# aidan
# aoc2024 day17
#

import re

lines = []

with open('input/day17.txt') as f:
    for line in f:
        lines.append(line.strip())

registers = [0, 0, 0]
instructions = None

for line in lines:
    if 'A' in line : registers[0] = int(re.findall("\d+", line)[0])
    elif 'B' in line : registers[1] = int(re.search("\d+", line)[0])
    elif 'C' in line : registers[2] = int(re.search("\d+", line)[0])
    elif line : instructions = [int(tok) for tok in re.findall("\d+", line)]

registers_og = [tok for tok in registers]

output=[]
ptr = 0
while ptr < len(instructions):
    opcode_num = instructions[ptr]
    operand_num = instructions[ptr + 1]
    ptr += 2
    combo_operand_num = {
        0:0, 1:1, 2:2, 3:3,
        4:registers[0],
        5:registers[1],
        6:registers[2]
    }[operand_num]
    if opcode_num == 0:
        numerator = registers[0]
        denominator = 2**combo_operand_num
        registers[0] = numerator // denominator
    elif opcode_num == 1:
        registers[1] ^= operand_num
    elif opcode_num == 2:
        registers[1] = combo_operand_num % 8
    elif opcode_num == 3:
        if registers[0] == 0:
            continue
        ptr = operand_num
    elif opcode_num == 4:
        registers[1] ^= registers[2]
    elif opcode_num == 5:
        output.append(str(combo_operand_num % 8))
    elif opcode_num == 6:
        numerator = registers[0]
        denominator = 2**combo_operand_num
        registers[1] = numerator // denominator
    elif opcode_num == 7:
        numerator = registers[0]
        denominator = 2**combo_operand_num
        registers[2] = numerator // denominator

# part 1
ans_p1 = ','.join(output)
print(f"\nFirst Problem Solution: {ans_p1}")

output_og = [tok for tok in output]

cntr = 100
while cntr >= 0:
    output = []
    ptr = 0
    registers = [tok for tok in registers_og]
    registers[0] = cntr
    while ptr < len(instructions):
        opcode_num = instructions[ptr]
        operand_num = instructions[ptr + 1]
        ptr += 2
        combo_operand_num = {
            0:0, 1:1, 2:2, 3:3,
            4:registers[0],
            5:registers[1],
            6:registers[2]
        }[operand_num]
        if opcode_num == 0:
            numerator = registers[0]
            denominator = 2**combo_operand_num
            registers[0] = numerator // denominator
        elif opcode_num == 1:
            registers[1] ^= operand_num
        elif opcode_num == 2:
            registers[1] = combo_operand_num % 8
        elif opcode_num == 3:
            if registers[0] == 0:
                continue
            ptr = operand_num
        elif opcode_num == 4:
            registers[1] ^= registers[2]
        elif opcode_num == 5:
            output.append(str(combo_operand_num % 8))
        elif opcode_num == 6:
            numerator = registers[0]
            denominator = 2**combo_operand_num
            registers[1] = numerator // denominator
        elif opcode_num == 7:
            numerator = registers[0]
            denominator = 2**combo_operand_num
            registers[2] = numerator // denominator
    if ','.join(output) == ','.join([str(i) for i in instructions]):
        break
    if len(output) < len(instructions):
        cntr = int(cntr * 1.1)
        continue
    arr1 = list(reversed([str(i) for i in instructions]))
    arr2 = list(reversed(output))
    factor = 10000000000
    for i, val in enumerate(arr1):
        if val == arr2[i]:
            factor //= 10
        else : break
    cntr += max(factor, 1)

# part 2
ans_p2 = cntr
print(f"\nSecond Problem Solution: {ans_p2}\n")
