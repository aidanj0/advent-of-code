# aidan
# aoc2024 day05
#

lines = []

with open('input/day05.txt') as f:
    for line in f:
        lines.append(line)

befores = {}
afters = {}
successes = []
fails = []
redones = []

for line in lines:
    if '|' in line:
        b, a = (int(i) for i in line.strip().split('|'))
        if b not in befores : befores[b] = []
        if a not in afters : afters[a] = []
        befores[b].append(a)
        afters[a].append(b)
    elif ',' in line:
        pages = [int(i) for i in line.strip().split(',')]
        fflag = True
        for i in range(len(pages)):
            curr = pages[i]
            prefix = pages[:i]
            suffix = pages[i+1:]
            flag = True
            for page in prefix:
                if curr not in afters or page not in afters[curr]:
                    flag = False
            for page in suffix:
                if curr not in befores or page not in befores[curr]:
                    flag = False
            if not flag:
                fflag = False
                break
        if fflag:
            successes.append(pages)
        else:
            fails.append(pages)

for fail in fails:
    seen = {tuple(fail)}
    ffails = [fail]
    while ffails:
        pages = ffails.pop()
        fflag = True
        for i in range(len(pages)):
            curr = pages[i]
            prefix = pages[:i]
            suffix = pages[i+1:]
            flag = True
            for page in prefix:
                if curr not in afters or page not in afters[curr]:
                    flag = False
                    for j in range(len(prefix)):
                        newpages = prefix[:j] + [curr] + prefix[j:] + suffix
                        if len(prefix) == 1: newpages = [curr] + prefix + suffix
                        if tuple(newpages) not in seen:
                            seen.add(tuple(newpages))
                            ffails.append(newpages)
                    break
            for page in suffix:
                if curr not in befores or page not in befores[curr]:
                    flag = False
                    for j in range(1,len(suffix)+1):
                        newpages = prefix + suffix[:j] + [curr] + suffix[j:]
                        if len(suffix) == 1: newpages = prefix + suffix + [curr]
                        if tuple(newpages) not in seen:
                            seen.add(tuple(newpages))
                            ffails.append(newpages)
                    break
            if not flag:
                fflag = False
                break
        if fflag:
            redones.append(pages)
            break

# part 1
ans_p1 = 0
for row in successes:
    ans_p1 += row[len(row)//2]
print(f"\nFirst Problem Solution: {ans_p1}")

# part 2
ans_p2 = 0
for row in redones:
    ans_p2 += row[len(row)//2]
print(f"\nSecond Problem Solution: {ans_p2}\n")
