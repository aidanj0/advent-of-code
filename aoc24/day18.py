# aidan
# aoc2024 day18
#

lines = []

with open('input/day18.txt') as f:
    for line in f:
        lines.append(line.strip())

grid = [ ['.' for j in range(71)] for i in range(71) ]

for line in lines[:1024]:
    col, row = (int(tok) for tok in line.split(','))
    grid[row][col] = '#'

frontier = [(0, 0, 0)]
seen = {(0, 0)}
final_score = None
while frontier and final_score is None:
    row, col, score = frontier.pop(0)
    ops = [
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1)
    ]
    for op in ops:
        try:
            ro, co = op
            if ro < 0 or co < 0 : raise Exception
            if grid[ro][co] == '.' and (ro, co) not in seen:
                frontier.append((ro, co, score + 1))
                seen.add((ro, co))
            if grid[ro][co] == '.' and ro == 70 and co == 70:
                final_score = score + 1
        except:
            pass

# part 1
ans_p1 = final_score
print(f"\nFirst Problem Solution: {ans_p1}")

for line in lines[1024:]:
    col, row = (int(tok) for tok in line.split(','))
    grid[row][col] = '#'
    frontier = [(0, 0, 0)]
    seen = {(0, 0)}
    final_score = None
    while frontier and final_score is None:
        row, col, score = frontier.pop(0)
        ops = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1)
        ]
        for op in ops:
            try:
                ro, co = op
                if ro < 0 or co < 0 : raise Exception
                if grid[ro][co] == '.' and (ro, co) not in seen:
                    frontier.append((ro, co, score + 1))
                    seen.add((ro, co))
                if grid[ro][co] == '.' and ro == 70 and co == 70:
                    final_score = score + 1
            except:
                pass
    if final_score is None:
        p2ans=line
        break

# part 2
print(f"\nSecond Problem Solution: {p2ans}\n")
