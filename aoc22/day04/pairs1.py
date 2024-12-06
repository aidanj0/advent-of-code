with open('./day04/pairs.txt') as f:
    score = 0
    for line in f:
        s = line.strip()
        ps = s.split(',')
        p1 = ps[0].split('-')
        p2 = ps[1].split('-')
        a = int(p1[0])
        b = int(p1[1])
        c = int(p2[0])
        d = int(p2[1])
        if (a <= d and c <= b) or (c <= b and a <= d):
            score += 1
    print(score)