# aidan
# aoc2024 day10
#

lines = []

with open('input/day10.txt') as f:
    for line in f:
        lines.append(line.strip())

grid = []

for line in lines:
    grid.append([])
    for c in line:
        grid[-1].append(int(c))

adj_map = {}
adj_map_reverse = {}
height_ind_map = {}

for row_i in range(len(grid)):
    for col_j in range(len(grid[0])):
        curr_height = grid[row_i][col_j]
        height_ind_map.setdefault(curr_height, []).append((row_i, col_j))
        for row_i1, col_j1 in (
            (row_i + 1, col_j),
            (row_i - 1, col_j),
            (row_i, col_j + 1),
            (row_i, col_j - 1)
        ):
            if row_i1 >= 0 and col_j1 >= 0:
                try:
                    opt_height = grid[row_i1][col_j1]
                    if opt_height == curr_height + 1:
                        adj_map.setdefault((row_i, col_j), []).append((row_i1, col_j1))
                        adj_map_reverse.setdefault((row_i1, col_j1), []).append((row_i, col_j))
                except : pass

scoring_map = {}

for val in range(8, -1, -1):
    for posn in height_ind_map[val]:
        if val == 8 and posn in adj_map:
            scoring_map[posn] = {p for p in adj_map[posn]}
        elif posn in adj_map:
            locs = set()
            for p in adj_map[posn]:
                if p in scoring_map : locs = locs.union(scoring_map[p])
            scoring_map[posn] = locs

cnt = 0
for zero_posn in height_ind_map[0]:
    if zero_posn in scoring_map:
        cnt += len(scoring_map[zero_posn])

# part 1
ans_p1 = cnt
print(f"\nFirst Problem Solution: {ans_p1}")

dp = {}
for posn in height_ind_map[9]:
    if posn in adj_map_reverse:
        dp[posn] = 1
p2sum = 0

for i in range(8, -1, -1):
    for posn_curr in height_ind_map[i]:
        if posn_curr not in adj_map:
            dp[posn_curr] = 0
            continue # if this doesn't go anywhere
        curr_total = 0
        for posn_above in adj_map[posn_curr]:
            curr_total += dp[posn_above]
        dp[posn_curr] = curr_total
        if i == 0 : p2sum += curr_total

# part 2
ans_p2 = p2sum
print(f"\nSecond Problem Solution: {ans_p2}\n")
