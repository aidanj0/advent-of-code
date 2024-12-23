# aidan
# aoc2024 day13
#

import re
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

cnt = 0

while games:
    a, b, p = games.pop()
    ax, ay = a
    bx, by = b
    px, py = p
    best_cost = math.inf
    for i in range(99999999):
        pxi, pyi = (px - i*ax, py - i*ay)
        if pxi < 0 or pyi < 0 : break
        if pxi % bx == 0 and pyi % by == 0 and pxi // bx == pyi // by:
            cost = i * 3 + pxi // bx
            best_cost = min(cost, best_cost)
    for i in range(99999999):
        pxi, pyi = (px - i*bx, py - i*by)
        if pxi < 0 or pyi < 0 : break
        if pxi % ax == 0 and pyi % ay == 0 and pxi // ax == pyi // ay:
            cost = i + (pxi // ax) * 3
            best_cost = min(cost, best_cost)
    if best_cost != math.inf : cnt += best_cost

# part 1
ans_p1 = cnt
print(f"\nFirst Problem Solution: {ans_p1}")

# part 2
ans_p2 = 0
print(f"\nSecond Problem Solution: {ans_p2}\n")
