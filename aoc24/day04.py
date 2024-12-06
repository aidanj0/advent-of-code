# aidan
# aoc2024 day04, written 2024/12/04
#

grid = []

with open('input/day04.txt') as f:
    for line in f:
        grid.append(line.strip())

frontier = []

for row_i in range(len(grid)):
    for col_j in range(len(grid[0])):
        curr = grid[row_i][col_j]
        if curr == 'X':
            frontier.append(('X', row_i, col_j, None))

ans_p1 = 0
while frontier:
    s, i, j, opt = frontier.pop()
    des = ''
    if s == 'X' : des = 'M'
    elif s == 'M' : des = 'A'
    elif s == 'A' : des = 'S'
    options = [
        (1, 1),
        (1, 0),
        (1, -1),
        (0, 1),
        (0, -1),
        (-1, 1),
        (-1, 0),
        (-1, -1)
    ] if (opt == None) else [opt]
    for option in options:
        try:
            option_i = i + option[0]
            option_j = j + option[1]
            if option_i != -1 and option_j != -1:
                option_char = grid[option_i][option_j]
                if option_char == des and des == 'S':
                    ans_p1 += 1
                elif option_char == des:
                    frontier.append((des, option_i, option_j, option))
        except:
            pass
print(f"\nFirst Problem Solution: {ans_p1}")

ans_p2 = 0
for row_i in range(len(grid)):
    for col_j in range(len(grid[0])):
        curr = grid[row_i][col_j]
        if curr == 'A':
            frontier.append((row_i, col_j))

while frontier:
    i, j = frontier.pop()
    spots = [
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
    opts = [ (i + x, j + y) for x, y in spots ]
    opts_n = []
    for opt in opts:
        if -1 not in opt : opts_n.append(opt)
    if len(opts_n) == 4:
        try:
            tl = grid[i - 1][j - 1]
            tr = grid[i - 1][j + 1]
            bl = grid[i + 1][j - 1]
            br = grid[i + 1][j + 1]
            set1 = {tl, br}
            set2 = {tr, bl}
            if 'M' in set1.intersection(set2) and 'S' in set1.intersection(set2):
                ans_p2 += 1
        except:
            pass
print(f"\nSecond Problem Solution: {ans_p2}\n")
