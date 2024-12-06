lines = []
with open('./day13/packets.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

i = 0
score = 0
while lines:
    i += 1
    l1s = lines.pop(0)
    l2s = lines.pop(0)
    if lines : lines.pop(0)
    decoded = []
    for line in [l1s, l2s]:
        ln = []
        line = line[1:-1]
        curr = ln
        formercurr = []
        while line:
            if line[0] == '[':
                curr.append([])
                formercurr.append(curr)
                curr = curr[-1]
                line = line[1:]
            elif line[0] == ',':
                line = line[1:]
            elif line[0] == ']':
                curr = formercurr.pop()
                line = line[1:]
            else:
                strnum = line.split(',')[0]
                strnum = strnum.split(']')[0]
                num = int(strnum)
                curr.append(num)
                line = line[len(strnum):]
        decoded.append(ln)

    flag = True
    left = decoded[0]
    right = decoded[1]
    frontier = [left, right]
    while frontier:
        l = frontier.pop(0)
        r = frontier.pop(0)
        if type(l) == int and type(r) == int:
            if l > r:
                flag = False
                break
            elif l < r:
                break
        elif type(l) == int and type(r) == list:
            frontier.insert(0, r)
            frontier.insert(0, [l])
        elif type(l) == list and type(r) == int:
            frontier.insert(0, [r])
            frontier.insert(0, l)
        else:
            if l and r:
                l_first = l.pop(0)
                r_first = r.pop(0)
                frontier.insert(0, r)
                frontier.insert(0, l)
                frontier.insert(0, r_first)
                frontier.insert(0, l_first)
            elif r and not l:
                break
            elif l and not r:
                flag = False
                break
            else : pass
    if flag : score += i

print(score)