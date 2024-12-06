lines = []
with open('./day10/signals.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

i = 0
val = 1
sums = 0
buffer = []

for line in lines:
    if i in {20, 60, 100, 140, 180, 220}:
        sums += (i * val)
    if buffer : val += buffer.pop(0)
    if line == 'noop' : buffer.append(0)
    else:
        num = int(line.split(' ')[1])
        buffer += [0, num]
    i += 1

while buffer:
    if i in {20, 60, 100, 140, 180, 220}:
        sums += (i * val)
    val += buffer.pop(0)
    i += 1
print(sums)