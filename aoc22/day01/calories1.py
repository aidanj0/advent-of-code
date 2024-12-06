with open('./day01/calories.txt') as f:
    curr = 0
    best = -1
    for line in f:
        s = line.strip()
        if s:
            curr += int(s)
        else:
            best = max(best, curr)
            curr = 0
    print(best) # 69310