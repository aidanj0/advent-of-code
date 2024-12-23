# aidan
# aoc2024 day11
#

lines = []

with open('input/day11.txt') as f:
    for line in f:
        lines.append(line.strip())

stones = lines[0].split()

for i in range(25):
    new_stones = []
    while stones:
        stone = stones.pop(0)
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            new_stones.append(str(int(stone[:len(stone) // 2])))
            new_stones.append(str(int(stone[len(stone) // 2:])))
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = new_stones

# part 1
ans_p1 = len(stones)
print(f"\nFirst Problem Solution: {ans_p1}\n")

lines = []

with open('input/day11.txt') as f:
    for line in f:
        lines.append(line.strip())

stones = lines[0].split()

stone_map = { stone: stones.count(stone) for stone in set(stones) }
for i in range(75):
    new_stone_map = {}
    while stone_map:
        stone, occ = stone_map.popitem()
        if stone == '0':
            if '1' not in new_stone_map : new_stone_map['1'] = occ
            else: new_stone_map['1'] += occ
        elif len(stone) % 2 == 0:
            if str(int(stone[:len(stone) // 2])) not in new_stone_map : new_stone_map[str(int(stone[:len(stone) // 2]))] = occ
            else: new_stone_map[str(int(stone[:len(stone) // 2]))] += occ
            if str(int(stone[len(stone) // 2:])) not in new_stone_map : new_stone_map[str(int(stone[len(stone) // 2:]))] = occ
            else: new_stone_map[str(int(stone[len(stone) // 2:]))] += occ
        else:
            if str(int(stone) * 2024) not in new_stone_map : new_stone_map[str(int(stone) * 2024)] = occ
            else : new_stone_map[str(int(stone) * 2024)] += occ
    stone_map = new_stone_map

# part 2
ans_p2 = 0
while stone_map:
    stone, occ = stone_map.popitem()
    ans_p2 += occ
print(f"Second Problem Solution: {ans_p2}\n")
