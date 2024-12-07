# aidan
# aoc2024 day07
#

lines = []

with open('input/day07.txt') as f:
    for line in f:
        lines.append(line.strip())

cnt = 0

for line in lines:
    halves = line.split(': ')
    val = int(halves[0])
    nums = [int(i) for i in halves[1].split(' ')]
    track = {0: [nums[0]]}
    for i in range(1, len(nums)):
        track[i] = []
        for value in track[i-1]:
            track[i].append(nums[i] * value)
            track[i].append(nums[i] + value)
    if val in track[len(nums) - 1]:
        cnt += val

# part 1
ans_p1 = cnt
print(f"\nFirst Problem Solution: {ans_p1}")

cnt2 = 0

for line in lines:
    halves = line.split(': ')
    val = int(halves[0])
    nums = [int(i) for i in halves[1].split(' ')]
    track = {0: [nums[0]]}
    for i in range(1, len(nums)):
        track[i] = []
        for value in track[i-1]:
            track[i].append(nums[i] * value)
            track[i].append(nums[i] + value)
            track[i].append(int(str(value)+str(nums[i])))
    if val in track[len(nums) - 1]:
        cnt2 += val

# part 2
ans_p2 = cnt2
print(f"\nSecond Problem Solution: {ans_p2}\n")
