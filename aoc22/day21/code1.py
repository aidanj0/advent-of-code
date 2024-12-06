lines = []
with open('./day21/input.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

hm = {}
while lines:
    line = lines.pop(0)
    mc = line[0:4]
    if line[6] in '0123456789' : hm[mc] = int(line[6:])
    else :
        m1 = line.split(': ')[1].split(' ')[0]
        m2 = line.split(': ')[1].split(' ')[-1]
        op = line.split(': ')[1].split(' ')[1]
        if m1 in hm and m2 in hm:
            if op == '+' : hm[mc] = hm[m1] + hm[m2]
            elif op == '-' : hm[mc] = hm[m1] - hm[m2]
            elif op == '*' : hm[mc] = hm[m1] * hm[m2]
            else : hm[mc] = hm[m1] // hm[m2]
        else : lines.append(line)