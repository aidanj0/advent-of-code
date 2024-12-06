# aidan
# aoc2024 day01, rewritten 2024/12/03
#

one = []
two = []

with open('input/day01.txt') as f:
    for line in f:
        s = line.strip().split('   ')
        n1 = int(s[0])
        n2 = int(s[1])
        one.append(n1)
        two.append(n2)

# part 1
ans_p1 = 0
one_sorted = list(sorted(one))
two_sorted = list(sorted(two))
for i in range(len(one_sorted)):
    ans_p1 += abs(one_sorted[i] - two_sorted[i])
print(f"\nFirst Problem Solution: {ans_p1}")

# part 2
ans_p2 = 0
for tok in one:
    if tok in two:
        ans_p2 += tok * two.count(tok)
print(f"\nSecond Problem Solution: {ans_p2}\n")
