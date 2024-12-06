import math

lines = []
with open('./day12/heightmap.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

end = ()
starts = []
matrix = []
lookup = 'abcdefghijklmnopqrstuvwxyz'
hm = {}
for i in range(26) : hm[lookup[i]] = i
hm['S'] = 0
hm['E'] = 25
for line in lines:
    matrix.append([hm[c] for c in line])
    for i in range(len(matrix[-1])):
        if matrix[-1][i] == 0 : starts.append((len(matrix) - 1, i))
    if 'E' in line:
        end = (len(matrix) - 1, line.index('E'))

best = math.inf
for start in starts:
    queue = [start + tuple([0])]
    seen = set(start)
    while queue:
        nr, nc, dist = queue.pop(0)
        if (nr, nc) == end:
            best = min(best, dist)
        tile = matrix[nr][nc]
        if nr > 0 and (nr - 1, nc) not in seen and matrix[nr - 1][nc] <= tile + 1:
            queue.append((nr - 1, nc, dist + 1))
            seen.add((nr - 1, nc))
        if nc > 0 and (nr, nc - 1) not in seen and matrix[nr][nc - 1] <= tile + 1:
            queue.append((nr, nc - 1, dist + 1))
            seen.add((nr, nc - 1))
        if nr < len(matrix) - 1 and (nr + 1, nc) not in seen and matrix[nr + 1][nc] <= tile + 1:
            queue.append((nr + 1, nc, dist + 1))
            seen.add((nr + 1, nc))
        if nc < len(matrix[0]) - 1 and (nr, nc + 1) not in seen and matrix[nr][nc + 1] <= tile + 1:
            queue.append((nr, nc + 1, dist + 1))
            seen.add((nr, nc + 1))
print(best)