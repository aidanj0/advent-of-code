import copy

with open('./day17/rocks.txt') as f:
    for line in f:
        s = line.strip()
        gusts = [c for c in s]

rocks = [
    [
        [ '#', '.', '.', '@', '@', '@', '@', '.', '#' ],
    ],
    [
        [ '#', '.', '.', '.', '@', '.', '.', '.', '#' ],
        [ '#', '.', '.', '@', '@', '@', '.', '.', '#' ],
        [ '#', '.', '.', '.', '@', '.', '.', '.', '#' ]
    ],
    [
        [ '#', '.', '.', '.', '.', '@', '.', '.', '#' ],
        [ '#', '.', '.', '.', '.', '@', '.', '.', '#' ],
        [ '#', '.', '.', '@', '@', '@', '.', '.', '#' ]
    ],
    [
        [ '#', '.', '.', '@', '.', '.', '.', '.', '#' ],
        [ '#', '.', '.', '@', '.', '.', '.', '.', '#' ],
        [ '#', '.', '.', '@', '.', '.', '.', '.', '#' ],
        [ '#', '.', '.', '@', '.', '.', '.', '.', '#' ]
    ],
    [
        [ '#', '.', '.', '@', '@', '.', '.', '.', '#' ],
        [ '#', '.', '.', '@', '@', '.', '.', '.', '#' ]
    ],
]

empty_layer = [ '#', '.', '.', '.', '.', '.', '.', '.', '#' ]

rocks_dropped = 0
gusts_tossed = 0
chamber = [ [ '#' for i in range(9) ] ]
while rocks_dropped < 2022:
    while '#' not in chamber[0][1:8]:
        chamber.pop(0)
    for i in range(3) : chamber.insert(0, copy.deepcopy(empty_layer))
    for i in range(len(rocks[rocks_dropped % 5]) - 1, -1, -1):
        chamber.insert(0, copy.deepcopy(rocks[rocks_dropped % 5][i]))
    rock_posns = []
    for row in range(4):
        for col in range(9):
            if chamber[row][col] == '@' : rock_posns.append([row, col])
    still_falling = True
    while still_falling:
        # try to move left/right according to gust of wind
        gust = gusts[gusts_tossed % len(gusts)]
        col_delta = -1 if gust == '<' else 1
        p_rock_posns = []
        for rp in rock_posns:
            if chamber[rp[0]][rp[1] + col_delta] != '#':
                p_rock_posns.append([rp[0], rp[1] + col_delta])
        if len(rock_posns) == len(p_rock_posns):
            for rp in rock_posns:
                chamber[rp[0]][rp[1]] = '.'
            for prp in p_rock_posns:
                chamber[prp[0]][prp[1]] = '@'
            rock_posns = p_rock_posns
        gusts_tossed += 1
        # try to move down
        p_rock_posns = []
        for rp in rock_posns:
            if chamber[rp[0] + 1][rp[1]] != '#':
                p_rock_posns.append([rp[0] + 1, rp[1]])
        if len(rock_posns) == len(p_rock_posns):
            for rp in rock_posns:
                chamber[rp[0]][rp[1]] = '.'
            for prp in p_rock_posns:
                chamber[prp[0]][prp[1]] = '@'
            rock_posns = p_rock_posns
        else:
            still_falling = False
            for rp in rock_posns:
                chamber[rp[0]][rp[1]] = '#'
    rocks_dropped += 1

print(len( [ row for row in chamber if '#' in row[1:8] ] ) - 1)