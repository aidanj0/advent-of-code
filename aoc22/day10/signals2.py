lines = []
with open('./day10/signals.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

i = 0
val = 1
buffer = []
draw = [[] for i in range(6)]

for line in lines:
    draw[i // 40].append('#' if abs(val - (i % 40)) < 2 else '.')
    if line == 'noop' : buffer.append(0)
    else:
        num = int(line.split(' ')[1])
        buffer += [0, num]
    val += buffer.pop(0)
    i += 1

while buffer:
    draw[i // 40].append('#' if abs(val - (i % 40)) < 2 else '.')
    val += buffer.pop(0)
    i += 1
for d in draw:
    print(d)