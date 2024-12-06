import functools
import copy

lines = []
with open('./day13/packets.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

div1 = [[2]]
div2 = [[6]]
packets = [ div1, div2 ]
while lines:
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
        packets.append(ln)

def compare_packets(left, right):
    left = copy.deepcopy(left)
    right = copy.deepcopy(right)
    res = 0
    frontier = [left, right]
    while frontier:
        l = frontier.pop(0)
        r = frontier.pop(0)
        if type(l) == int and type(r) == int:
            if l > r:
                res = -1
                break
            elif l < r:
                res = 1
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
                res = 1
                break
            elif l and not r:
                res = -1
                break
            else : pass
    return -res

packets.sort(key=functools.cmp_to_key(compare_packets))
print((packets.index(div1) + 1) * (packets.index(div2) + 1))