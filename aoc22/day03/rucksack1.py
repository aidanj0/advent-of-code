with open('./day03/rucksack.txt') as f:
    score = 0
    lookup = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sets = []
    for line in f:
        s = line.strip()
        part1 = set(s[:len(s) // 2])
        part2 = set(s[len(s) // 2:])
        item = (part1 & part2).pop()
        score += lookup.index(item)
    print(score)