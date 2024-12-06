with open('./day03/rucksack.txt') as f:
    score = 0
    lookup = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sets = []
    for line in f:
        s = line.strip()
        if len(sets) < 3:
            sets.append(set(s))
        else:
            totalset = sets[0] & sets[1] & sets[2]
            item = totalset.pop()
            score += lookup.index(item)
            sets = [set(s)]
    score += lookup.index((sets[0] & sets[1] & sets[2]).pop())
    print(score)