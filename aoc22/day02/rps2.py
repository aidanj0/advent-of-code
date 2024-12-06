with open('./day02/rps.txt') as f:
    score = 0
    for line in f:
        s = line.strip()
        spl = s.split(' ')
        opp = spl[0]
        me = spl[1]
        if opp == 'A':
            score += {'X' : 3, 'Y' : 4, 'Z' : 8}[me]
        elif opp == 'B':
            score += {'X' : 1, 'Y' : 5, 'Z' : 9}[me]
        else:
            score += {'X' : 2, 'Y' : 6, 'Z' : 7}[me]
    print(score) # 14859