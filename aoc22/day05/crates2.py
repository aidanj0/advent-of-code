with open('./day05/crates.txt') as f:
    hm = {
        1 : [x for x in 'RHMPZ'],
        2 : [x for x in 'BJCP'],
        3 : [x for x in 'DCLGHNS'],
        4 : [x for x in 'LRSQDMTF'],
        5 : [x for x in 'MZTBQPSF'],
        6 : [x for x in 'GHZSFT'],
        7 : [x for x in 'VRN'],
        8 : [x for x in 'MCVDTLGP'],
        9 : [x for x in 'LMFJNQW']
    }
    for line in f:
        s = line.strip()
        if s and s[0] == 'm':
            arr = s.split(' ')
            amt = int(arr[1])
            frm = int(arr[3])
            to = int(arr[5])
            blocks = []
            for i in range(amt):
                blocks.append(hm[frm].pop(0))
            blocks.reverse()
            for i in range(amt):
                hm[to].insert(0, blocks.pop(0))
    res = ''
    for v in hm.values():
        res += v[0]
    print(res)