lines = []
with open('./day09/knots.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

hp = [0, 0]
tp = [0, 0]
seen = {tuple(tp)}
for line in lines:
    if line[0] == 'D' : hp[1] -= int(line.split(' ')[1])
    elif line[0] == 'U' : hp[1] += int(line.split(' ')[1])
    elif line[0] == 'L' : hp[0] -= int(line.split(' ')[1])
    elif line[0] == 'R' : hp[0] += int(line.split(' ')[1])
    while abs(hp[0] - tp[0]) > 1 or abs(hp[1] - tp[1]) > 1:
        if hp[0] == tp[0] and hp[1] > tp[1]: # tail below head
            tp[1] += 1
        elif hp[0] == tp[0] and hp[1] < tp[1]: # tail above head
            tp[1] -= 1
        elif hp[1] == tp[1] and hp[0] > tp[0]: # tail to the left of head
            tp[0] += 1
        elif hp[1] == tp[1] and hp[0] < tp[0]: # tail to the right of head
            tp[0] -= 1
        elif hp[0] > tp[0] and hp[1] > tp[1]: # tail below and to the left of head
            tp[0] += 1
            tp[1] += 1
        elif hp[0] < tp[0] and hp[1] < tp[1]: # tail above and to the right of head
            tp[0] -= 1
            tp[1] -= 1
        elif hp[0] > tp[0] and hp[1] < tp[1]: # tail above and to the left of head
            tp[0] += 1
            tp[1] -= 1
        elif hp[0] < tp[0] and hp[1] > tp[1]: # tail below and to the right of head
            tp[0] -= 1
            tp[1] += 1
        seen.add(tuple(tp))
print(len(seen))