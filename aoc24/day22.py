# aidan
# aoc2024 day22
#

lines = []

with open('input/day22.txt') as f:
    for line in f:
        lines.append(line.strip())

initial = []

for line in lines:
    initial.append(int(line))

sums = 0
secrets = []

for num in initial:
    secret = num
    secrets.append([secret])
    for i in range(2000):
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ (secret // 32)) % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        secrets[-1].append(secret)
    sums += secret

# part 1
ans_p1 = sums
print(f"\nFirst Problem Solution: {ans_p1}")

changes_overall = {}

for i in range(len(initial)):
    curr_secrets = secrets[i]
    curr_changes = {}
    for j in range(5, len(curr_secrets)):
        curr_range = [int(str(tok)[-1]) for tok in curr_secrets[j-5:j]]
        curr_diffs = []
        for k in range(1, 5):
            curr_diffs.append(curr_range[k] - curr_range[k-1])
        curr_diffs = tuple(curr_diffs)
        price = curr_range[-1]
        price = int(str(price)[-1])
        if curr_diffs not in curr_changes:
            curr_changes[curr_diffs] = price
    for key, val in curr_changes.items():
        changes_overall.setdefault(key, []).append(val)

greedy = -1
for key, val in changes_overall.items():
    greedy = max(greedy, sum(val))

# part 2
ans_p2 = greedy
print(f"\nSecond Problem Solution: {ans_p2}\n")
