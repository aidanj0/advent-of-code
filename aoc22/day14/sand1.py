lines = []
with open('./day14/sand.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

matrix = [ ['.' for col in range(1000)] for row in range(1000) ]
for line in lines:
    nums = []
    for coord in line.split(' -> ') : nums += coord.split(',')
    if nums:
        c1 = int(nums.pop(0))
        r1 = int(nums.pop(0))
    while nums:
        c2 = int(nums.pop(0))
        r2 = int(nums.pop(0))
        if c1 == c2:
            for r in range(min(r1, r2), max(r1, r2) + 1):
                matrix[r][c1] = '#'
        elif r1 == r2:
            for c in range(min(c1, c2), max(c1, c2) + 1):
                matrix[r1][c] = '#'
        c1 = c2
        r1 = r2

score = 0
flag = True
while flag:
    sand = [0, 500]
    while True:
        row = sand[0]
        col = sand[1]
        if row == 999:
            flag = False
            break
        elif matrix[row + 1][col] == '.':
            sand[0] += 1
        elif matrix[row + 1][col - 1] == '.':
            sand[0] += 1
            sand[1] -= 1
        elif matrix[row + 1][col + 1] == '.':
            sand[0] += 1
            sand[1] += 1
        else:
            matrix[row][col] = 'o'
            score += 1
            break
print(score)