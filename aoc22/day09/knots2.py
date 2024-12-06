lines = []
with open('./day09/knots.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

knots = [ [0, 0] for i in range(10) ]
seen = { (0, 0) }
for line in lines:
    head = knots[0]
    if line[0] == 'D' : head[1] -= int(line.split(' ')[1])
    elif line[0] == 'U' : head[1] += int(line.split(' ')[1])
    elif line[0] == 'L' : head[0] -= int(line.split(' ')[1])
    elif line[0] == 'R' : head[0] += int(line.split(' ')[1])
    flag = True
    while flag:
        flag = False
        for i in range(1, 10):
            hp = knots[i - 1]
            tp = knots[i]
            if abs(hp[0] - tp[0]) > 1 or abs(hp[1] - tp[1]) > 1:
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
                flag = True
            if i == 9 : seen.add(tuple(tp))
print(len(seen))