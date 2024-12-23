# aidan
# aoc2024 day15
#

lines = []

with open('input/day15.txt') as f:
    for line in f:
        lines.append(line.strip())

grid = []
instrucs = ""
sub_posn = None

for line in lines:
    if '#' in line:
        grid.append([])
        for c in line:
            grid[-1].append(c)
    else : instrucs += line.strip()

for row_i in range(len(grid)):
    for col_j in range(len(grid[0])):
        if grid[row_i][col_j] == '@' : sub_posn = (row_i, col_j)

for instruc in instrucs:
    r, c = sub_posn
    if instruc == '>':
        ra, ca = (r, c + 1)
        item = grid[ra][ca]
        if item == '.':
            grid[r][c] = '.'
            grid[ra][ca] = '@'
            sub_posn = (ra, ca)
            continue
        if item == '#':
            continue
        if item == 'O':
            for col_j in range(ca, len(grid[0])):
                curr = grid[ra][col_j]
                if curr == '#':
                    break
                elif curr == 'O':
                    pass
                elif curr == '.':
                    grid[ra][col_j] = 'O'
                    grid[ra][ca] = '@'
                    grid[r][c] = '.'
                    sub_posn = (ra, ca)
                    break
    elif instruc == '<':
        ra, ca = (r, c - 1)
        item = grid[ra][ca]
        if item == '.':
            grid[r][c] = '.'
            grid[ra][ca] = '@'
            sub_posn = (ra, ca)
            continue
        if item == '#':
            continue
        if item == 'O':
            for col_j in range(ca, -1, -1):
                curr = grid[ra][col_j]
                if curr == '#':
                    break
                elif curr == 'O':
                    pass
                elif curr == '.':
                    grid[ra][col_j] = 'O'
                    grid[ra][ca] = '@'
                    grid[r][c] = '.'
                    sub_posn = (ra, ca)
                    break
    elif instruc == 'v':
        ra, ca = (r + 1, c)
        item = grid[ra][ca]
        if item == '.':
            grid[r][c] = '.'
            grid[ra][ca] = '@'
            sub_posn = (ra, ca)
            continue
        if item == '#':
            continue
        if item == 'O':
            for row_i in range(ra, len(grid)):
                curr = grid[row_i][ca]
                if curr == '#':
                    break
                elif curr == 'O':
                    pass
                elif curr == '.':
                    grid[row_i][ca] = 'O'
                    grid[ra][ca] = '@'
                    grid[r][c] = '.'
                    sub_posn = (ra, ca)
                    break
    elif instruc == '^':
        ra, ca = (r - 1, c)
        item = grid[ra][ca]
        if item == '.':
            grid[r][c] = '.'
            grid[ra][ca] = '@'
            sub_posn = (ra, ca)
            continue
        if item == '#':
            continue
        if item == 'O':
            for row_i in range(ra, -1, -1):
                curr = grid[row_i][ca]
                if curr == '#':
                    break
                elif curr == 'O':
                    pass
                elif curr == '.':
                    grid[row_i][ca] = 'O'
                    grid[ra][ca] = '@'
                    grid[r][c] = '.'
                    sub_posn = (ra, ca)
                    break

score = 0

for row_i in range(1, len(grid) - 1):
    for col_j in range(1, len(grid[0]) - 1):
        if grid[row_i][col_j] == 'O':
            score += col_j + (row_i * 100)

# part 1
ans_p1 = score
print(f"\nFirst Problem Solution: {ans_p1}")

# part 2
ans_p2 = 0
print(f"\nSecond Problem Solution: {ans_p2}\n")
