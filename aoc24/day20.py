# aidan
# aoc2024 day20
#

lines = []

with open('input/day20.txt') as f:
    for line in f:
        lines.append(line.strip())

grid = []

for line in lines:
    grid.append([])
    for c in line:
        grid[-1].append(c)

START = None
END = None

for row_i in range(len(grid)):
    for col_j in range(len(grid[0])):
        if grid[row_i][col_j] == 'S' : START = (row_i, col_j)
        if grid[row_i][col_j] == 'E' : END = (row_i, col_j)

# find length of the path
frontier = [(START, 0)]
seen = {START: 0}
path_tiles = [START]
while frontier:
    curr_posn, curr_time = frontier.pop()
    row, col = curr_posn
    opts = (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    )
    for opt in opts:
        rd, cd = opt
        tile = grid[row + rd][col + cd]
        tile_posn = (row + rd, col + cd)
        tile_time = curr_time + 1
        if (tile == '.' or tile == 'E') and tile_posn not in seen:
            seen[tile_posn] = tile_time
            path_tiles.append(tile_posn)
            frontier.append((tile_posn, tile_time))

skips_over_100 = set()
for i, tile_a in enumerate(path_tiles):
    for tile_b in path_tiles[i+1:]:
        ra, ca = tile_a
        rb, cb = tile_b
        delta = abs(rb - ra) + abs(cb - ca)
        if delta <= 2:
            time_save = seen[tile_b] - seen[tile_a]
            if time_save >= 100 + delta:
                skips_over_100.add((tile_a, tile_b))

# part 1
ans_p1 = len(skips_over_100)
print(f"\nFirst Problem Solution: {ans_p1}")

skips_over_100 = set()
for i, tile_a in enumerate(path_tiles):
    for tile_b in path_tiles[i+1:]:
        ra, ca = tile_a
        rb, cb = tile_b
        delta = abs(rb - ra) + abs(cb - ca)
        if delta <= 20:
            time_save = seen[tile_b] - seen[tile_a]
            if time_save >= 100 + delta:
                skips_over_100.add((tile_a, tile_b))

# part 2
ans_p2 = len(skips_over_100)
print(f"\nSecond Problem Solution: {ans_p2}\n")
