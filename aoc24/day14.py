# aidan
# aoc2024 day14
#

import re

lines = []

with open('input/day14.txt') as f:
    for line in f:
        lines.append(line.strip())

WIDE = 101
TALL = 103

grid = [ [ 0 for __ in range(WIDE) ] for _ in range(TALL) ]

a = 0
b = 0
c = 0
d = 0

for line in lines:
    dx, dy, vx, vy = tuple(int(i) for i in re.findall("-*\d+", line))
    dxf, dyf = (dx + (100 * vx), dy + (100 * vy))
    while dxf < 0 : dxf += WIDE
    while dxf >= WIDE : dxf -= WIDE
    while dyf < 0 : dyf += TALL
    while dyf >= TALL : dyf -= TALL
    grid[dyf][dxf] += 1
    if dyf < TALL // 2 and dxf < WIDE // 2:
        a += 1
    elif dyf > TALL //2 and dxf < WIDE // 2:
        b += 1
    elif dyf < TALL // 2 and dxf > WIDE // 2:
        c += 1
    elif dyf > TALL // 2 and dxf > WIDE // 2:
        d += 1

# part 1
ans_p1 = a*b*c*d
print(f"\nFirst Problem Solution: {ans_p1}")

output = ""
with open("outputa.txt", "w+") as file:
            file.write("")
seen = set()
# hacky solution with manual viewing, nabbed the tree from there
# noticed the trend of tall, grouped together chunks at 61+101x
for i in range(68, 999999999, 101):
    grid = [ [ ' ' for __ in range(WIDE) ] for _ in range(TALL) ]
    curr_output = ''
    for line in lines:
        dx, dy, vx, vy = tuple(int(j) for j in re.findall("-*\d+", line))
        dxf, dyf = (dx + (i * vx), dy + (i * vy))
        while dxf < 0 : dxf += WIDE
        while dxf >= WIDE : dxf -= WIDE
        while dyf < 0 : dyf += TALL
        while dyf >= TALL : dyf -= TALL
        grid[dyf][dxf] = '#'
    flag = 0
    for line in grid:
        curr_output += '|' + ''.join(line) + "|\n"
        if ''.join(line) == ''.join(reversed(line)):
            flag += 1
    if flag >= 0:
        with open("outputa.txt", "a") as file:
            file.writelines(curr_output + f'\n\n~{i}~\n\n')

# part 2
ans_p2 = 0
print(f"\nSecond Problem Solution: {ans_p2}\n")
