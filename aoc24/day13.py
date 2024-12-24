# aidan
# aoc2024 day13
#

import re
import numpy as np
import math

lines = []

with open('input/day13.txt') as f:
    for line in f:
        lines.append(line.strip())

games = []

for i in range(0, len(lines), 4):
    a = lines[i]
    b = lines[i + 1]
    p = lines[i + 2]
    ax, ay = ( int(re.search("(?<=X\+)\d*", a).group(0)), int(re.search("(?<=Y\+)\d*", a).group(0)) )
    bx, by = ( int(re.search("(?<=X\+)\d*", b).group(0)), int(re.search("(?<=Y\+)\d*", b).group(0)) )
    px, py = ( int(re.search("(?<=X\=)\d*", p).group(0)), int(re.search("(?<=Y\=)\d*", p).group(0)) )
    games.append( ( (ax, ay), (bx, by), (px, py) ) )

cnt1 = 0
cnt2 = 0

while games:
    a, b, p = games.pop()
    ax, ay = a
    bx, by = b
    px, py = p
    A = np.array([[ax, bx],[ay, by]])
    B = np.array([px, py])
    C = np.round(np.linalg.solve(A,B), decimals = 4)
    an, bn = tuple(C)
    if an*ax + bn*bx == px and an*ay + bn*by == py:
        cnt1 += int(3*an + bn)
    px += 10000000000000
    py += 10000000000000
    A = np.array([[ax, bx],[ay, by]])
    B = np.array([px, py])
    C = np.round(np.linalg.solve(A,B), decimals = 1)
    an, bn = tuple(C)
    if an*ax + bn*bx == px and an*ay + bn*by == py:
        cnt2 += int(3*an + bn)

# part 1
ans_p1 = cnt1
print(f"\nFirst Problem Solution: {ans_p1}")

# part 2
ans_p2 = cnt2
print(f"\nSecond Problem Solution: {ans_p2}\n")
