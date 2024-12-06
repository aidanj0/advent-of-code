posns = set()
with open('./day18/obsidian.txt') as f:
    for line in f:
        s = line.strip()
        posns.add( tuple( [ int(c) for c in s.split(',') ] ) )
res = 0
for posn in posns:
    for i in range(3):
        for d in [-1, 1]:
            sample = list(posn)
            sample[i] += d
            if tuple(sample) not in posns:
                res += 1

print(res)