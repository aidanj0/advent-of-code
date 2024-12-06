def pathify(path):
    res = ''
    for node in path:
        res += (node + ' ')
    return res[:-1]

edges = {}
base_values = {}

with open('./day07/filesystem.txt') as f:
    lines = []
    for line in f:
        s = line.strip()
        lines.append(s)

    lines.pop(0)
    path = ['/']
    while lines:
        line = lines.pop(0)
        if line == '$ ls':
            while lines and lines[0][0] != '$':
                l = lines.pop(0)
                if l[0] == 'd':
                    edges[pathify(path)] = edges.setdefault(pathify(path), []) + [pathify(path) + ' ' + l[4:]]
                    edges[pathify(path) + ' ' + l[4:]] = []
                else:
                    base_values[pathify(path)] = base_values.setdefault(pathify(path), 0) + int(l.split(' ')[0])
        elif line == '$ cd ..':
            path.pop()
        elif '$ cd ' in line:
            path.append(line[5:])

total_sum = 0
for start in edges.keys():
    frontier = [start]
    nsum = 0
    while frontier:
        node = frontier.pop()
        if node in base_values : nsum += base_values[node]
        if node in edges : frontier += edges[node]
    if nsum <= 100000:
        total_sum += nsum
print(total_sum)