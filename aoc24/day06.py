# aidan
# aoc2024 day06
#

grid = []

with open('input/day06.txt') as f:
    for line in f:
        grid.append(line)

start = None

for i_row in range(len(grid)):
    for j_col in range(len(grid[0])):
        if grid[i_row][j_col] == '^':
            start = (i_row, j_col)

seen = {start}
posn = start
direc = (-1, 0)
mapping = {
    (-1, 0) : (0, 1),
    (0, 1) : (1, 0),
    (1, 0) : (0, -1),
    (0, -1) : (-1, 0)
}

while True:
    curr = posn
    would_be = (posn[0] + direc[0], posn[1] + direc[1])
    if would_be[0] <= -1 or would_be[1] <= -1 or would_be[0] >= len(grid) or would_be[1] >= len(grid[0]):
        break
    would_be_thing = grid[would_be[0]][would_be[1]]
    if would_be_thing == '#':
        direc = mapping[direc]
    else:
        posn = would_be
        seen.add(would_be)

changes = []

for spot in seen:
    posn = start
    direc = (-1, 0)
    seen_hypo = {(posn, direc)}
    while True:
        curr = posn
        would_be = (posn[0] + direc[0], posn[1] + direc[1])
        if would_be[0] <= -1 or would_be[1] <= -1 or would_be[0] >= len(grid) or would_be[1] >= len(grid[0]):
            break
        would_be_thing = grid[would_be[0]][would_be[1]]
        if would_be_thing == '#' or would_be == spot:
            direc = mapping[direc]
            if (curr, direc) not in seen_hypo:
                seen_hypo.add((curr, direc))
            else:
                changes.append(spot)
                break
        else:
            if (would_be, direc) not in seen_hypo:
                posn = would_be
                seen_hypo.add((posn, direc))
            else:
                changes.append(spot)
                break

# part 1
ans_p1 = len(seen)
print(f"\nFirst Problem Solution: {ans_p1}")

# part 2
ans_p2 = len(changes)
print(f"\nSecond Problem Solution: {ans_p2}\n")
