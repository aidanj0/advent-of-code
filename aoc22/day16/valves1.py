lines = []
with open('./day16/valves.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

rates = {}
paths = {}
for line in lines:
    valve = line.split('Valve ')[1].split(' has')[0]
    rate = int(line.split('rate=')[1].split(';')[0])
    if ', ' in line : edges = line.split('valves ')[1].split(', ')
    else : edges = [line.split('valve ')[1]]
    rates[valve] = rate
    paths[valve] = edges

best = -1
frontier = [('AA', set(), 0, 0)]
leaderboard = {}
while frontier:
    valve, opened, time, score = frontier.pop()
    best = max(score, best)
    for p_valve in paths[valve]:
        if p_valve not in opened and rates[p_valve] != 0 and time <= 28:
            newopened = opened | { p_valve }
            if ( (p_valve, time + 2, frozenset(newopened)) in leaderboard and leaderboard[(p_valve, time + 2, frozenset(newopened))] < score + (rates[p_valve] * (30 - (time + 2))) ) or (p_valve, time + 2, frozenset(newopened)) not in leaderboard:
                frontier.append( (p_valve, newopened, time + 2, score + (rates[p_valve] * (30 - (time + 2)))) )
                leaderboard[(p_valve, time + 2, frozenset(newopened))] = score + (rates[p_valve] * (30 - (time + 2)))
        elif time <= 29:
            newopened = set() | opened
            if ( (p_valve, time + 1, frozenset(newopened)) in leaderboard and leaderboard[(p_valve, time + 1, frozenset(newopened))] < score ) or (p_valve, time + 1, frozenset(newopened)) not in leaderboard:
                frontier.append( (p_valve, newopened, time + 1, score) )
                leaderboard[(p_valve, time + 1, frozenset(newopened))] = score

print(best)