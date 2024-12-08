# aidan
# aoc2024 day08
#

lines = []

with open('input/day08.txt') as f:
    for line in f:
        lines.append(line.strip())

grid = lines
freq_locations = {}
for i_row in range(len(grid)):
    for j_col in range(len(grid[0])):
        val = grid[i_row][j_col]
        if val != '.':
            if val not in freq_locations : freq_locations[val] = []
            freq_locations[val].append((i_row, j_col))

saves = set()

for freq, locs in freq_locations.items():
    for loc_start in locs:
        for loc_other in locs:
            if loc_start == loc_other : continue
            delta = (loc_other[0] - loc_start[0], loc_other[1] - loc_start[1])
            other_pts = [(loc_other[0] + delta[0], loc_other[1] + delta[1])]
            for other_pt in other_pts:
                if other_pt[0] > -1 and other_pt[1] > -1:
                    try:
                        _ = grid[other_pt[0]][other_pt[1]]
                        saves.add(other_pt)
                    except:
                        pass
# part 1
ans_p1 = len(saves)
print(f"\nFirst Problem Solution: {ans_p1}")

for freq, locs in freq_locations.items():
    for loc_start in locs:
        for loc_other in locs:
            if loc_start == loc_other : continue
            delta = (loc_other[0] - loc_start[0], loc_other[1] - loc_start[1])
            other_pts = []
            for i in range(1, 100):
                other_pts.append((loc_other[0] + delta[0]*i, loc_other[1] + delta[1]*i))
            for i in range(-100, 0):
                other_pts.append((loc_other[0] + delta[0]*i, loc_other[1] + delta[1]*i))
            for other_pt in other_pts:
                if other_pt[0] > -1 and other_pt[1] > -1:
                    try:
                        _ = grid[other_pt[0]][other_pt[1]]
                        saves.add(other_pt)
                    except:
                        pass

# part 2
ans_p2 = len(saves)
print(f"\nSecond Problem Solution: {ans_p2}\n")
