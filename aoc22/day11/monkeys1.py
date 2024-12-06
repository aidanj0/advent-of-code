lines = []
with open('./day11/monkeys.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

monkeys = {}
mi = 0
for line in lines:
    if not line : pass
    elif line[0] == 'M': 
        monkeys[mi] = {}
        monkeys[mi]['score'] = 0
    elif line[0] == 'S' : monkeys[mi]['items'] = [ int(x) for x in line[16:].split(', ') ]
    elif line[0] == 'O':
        spl = line.split(' ')
        monkeys[mi]['op'] = ( spl[-2], int(spl[-1]) if spl[-1][0] in '0123456789' else spl[-1] )
    elif line[0] == 'T' : monkeys[mi]['div'] = int(line.split(' ')[-1])
    elif line[3] == 't' : monkeys[mi]['tc'] = int(line.split(' ')[-1])
    elif line[3] == 'f': 
        monkeys[mi]['fc'] = int(line.split(' ')[-1])
        mi += 1

for i in range(20):
    for mi in range(len(monkeys)):
        monkey = monkeys[mi]
        items = monkey['items']
        while items:
            monkey['score'] += 1
            item = items.pop(0)
            to_op = monkey['op'][-1] if type(monkey['op'][-1]) == int else item
            if monkey['op'][0] == '+' : item += to_op
            else : item *= to_op
            item //= 3
            if item % monkey['div'] == 0:
                monkeys[monkey['tc']]['items'].append(item)
            else : monkeys[monkey['fc']]['items'].append(item)

scores = list(sorted([ monkeys[mi]['score'] for mi in range(len(monkeys)) ]))
print(scores[-1] * scores[-2])