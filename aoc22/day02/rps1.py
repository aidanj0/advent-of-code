with open('./day02/rps.txt') as f:
    score = 0
    for line in f:
        s = line.strip()
        spl = s.split(' ')
        opp = spl[0]
        me = spl[1]
        if opp == 'A':
            score += {'X' : 4, 'Y' : 8, 'Z' : 3}[me]
        elif opp == 'B':
            score += {'X' : 1, 'Y' : 5, 'Z' : 9}[me]
        else:
            score += {'X' : 7, 'Y' : 2, 'Z' : 6}[me]
    print(score) # 10310