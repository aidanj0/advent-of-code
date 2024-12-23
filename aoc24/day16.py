# aidan
# aoc2024 day16
#

import heapq as hq
import math

lines = []

with open('input/day16.txt') as f:
    for line in f:
        lines.append(line.strip())

maze = []

for line in lines:
    maze.append([])
    for c in line:
        maze[-1].append(c)

START, END = None, None

for row_i in range(len(maze)):
    for col_j in range(len(maze[0])):
        if maze[row_i][col_j] == 'S' : START = (row_i, col_j)
        if maze[row_i][col_j] == 'E' : END = (row_i, col_j)

heap = [(0, START, (0, 1), {START})]  # (score, posn, direction)
bests = {(START, (0, 1)): 0}  # { (posn, direction) : score }
end_bests = math.inf
end_bests_set = set()
while heap:
    score, posn, direction, seen = hq.heappop(heap)
    r, c = posn
    rd, cd = direction
    possibles = []
    if (r + rd, c + cd) == END:
        if score + 1 == end_bests:
            end_bests_set = end_bests_set.union(seen)
        elif score + 1 < end_bests:
            end_bests_set.clear()
            end_bests_set = end_bests_set.union(seen)
        end_bests = min(score + 1, end_bests)
        continue
    if maze[r + rd][c + cd] != '#':
        possibles.append( (score + 1, (r + rd, c + cd), direction) )
    cw = {
        (0, 1) : (1, 0),  # r, c => c, -r
        (1, 0) : (0, -1),  # r, c => c, -r
        (0, -1) : (-1, 0),  # r, c => c, -r
        (-1, 0) : (0, 1)  # r, c => c, -r
    }
    ccw = {
        (0, 1) : (-1, 0),  # r, c => -c, r
        (-1, 0) : (0, -1),  # r, c => -c, r
        (0, -1) : (1, 0),  # r, c => -c, r
        (1, 0) : (0, 1)  # r, c => -c, r
    }
    possibles.append( (score + 1000, posn, (cd, -rd)) )
    possibles.append( (score + 1000, posn, (-cd, rd)) )
    for p_score, p_posn, p_direction in possibles:
        if (p_posn, p_direction) not in bests or p_score <= bests[(p_posn, p_direction)]:
            bests[(p_posn, p_direction)] = p_score
            p_seen = seen.union({p_posn})
            hq.heappush(heap, (p_score, p_posn, p_direction, p_seen) )

# part 1
ans_p1 = end_bests
print(f"\nFirst Problem Solution: {ans_p1}")

# part 2
ans_p2 = len(end_bests_set) + 1
print(f"\nSecond Problem Solution: {ans_p2}\n")
