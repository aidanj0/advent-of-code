with open('./day06/marker.txt') as f:
    for line in f:
        s = line.strip()
        for i in range(len(s)):
            if i >= 7:
                sub = s[i:i+14]
                if len(sub) == len(set([c for c in sub])):
                    print(i+14)
                    break