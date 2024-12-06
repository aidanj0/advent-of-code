posns = set()
with open('./day18/obsidian.txt') as f:
    for line in f:
        s = line.strip()
        posns.add( tuple( [ int(c) for c in s.split(',') ] ) )

max_x, max_y, max_z, min_x, min_y, min_z = [-1 for i in range(6)]
for posn in posns:
    max_x = max(max_x, posn[0])
    max_y = max(max_y, posn[1])
    max_z = max(max_z, posn[2])
    min_x = min(min_x, posn[0])
    min_y = min(min_y, posn[1])
    min_z = min(min_z, posn[2])

trapped = set()
res = 0
for posn in posns:
    for i in range(3):
        for d in [-1, 1]:
            sample = list(posn)
            sample[i] += d
            if tuple(sample) in posns:
                pass
            else:
                frontier = [tuple(sample)]
                seen = set()
                while frontier:
                    node = frontier.pop()
                    if node[0] > max_x or node[0] < min_x or node[1] > max_y or node[1] < min_y or node[2] > max_z or node[2] < min_z:
                        res += 1
                        break
                    for j in range(3):
                        for e in [-1, 1]:
                            sample = list(node)
                            sample[j] += e
                            if tuple(sample) not in seen and tuple(sample) not in posns:
                                frontier.append(tuple(sample))
                                seen.add(tuple(sample))

print(res)