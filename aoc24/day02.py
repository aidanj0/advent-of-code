# aidan
# aoc2024 day02, rewritten 2024/12/03
#

lines = []

with open('input/day02.txt') as f:
    for line in f:
        lines.append([int(i) for i in line.strip().split()])

def check_safe(line):
    diffs = []
    for i in range(len(line) - 1):
        diff = line[i] - line[i + 1]
        if abs(diff) < 1 or abs(diff) > 3 or (
            diffs and ((diffs[-1] < 0 and diff > 0) or (diffs[-1] > 0 and diff < 0))
        ):
            return False
        diffs.append(line[i] - line[i + 1])
    return True
    
# part 1
ans_p1 = 0
for line in lines:
    if check_safe(line) : ans_p1 += 1
print(f"\nFirst Problem Solution: {ans_p1}")

# part 2
ans_p2 = 0
for line in lines:
    if check_safe(line) : ans_p2 += 1
    else:
        flag = False
        for i in range(len(line)):
            alt = line[:i] + line[i + 1:]
            if check_safe(alt):
                flag = True
                break
        if flag : ans_p2 += 1
print(f"\nSecond Problem Solution: {ans_p2}\n")
