lines = []
with open('./day15/beacons.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

y_const = 2000000
zones = []
beacons = set()
for line in lines:
    sx = int(line.split('x=')[1].split(',')[0])
    sy = int(line.split('y=')[1].split(':')[0])
    bx = int(line.split('x=')[2].split(',')[0])
    by = int(line.split('y=')[2].split(':')[0])
    if by == y_const : beacons.add(bx)
    zones.append( { 'x' : sx, 'y' : sy, 'd' : abs(sx - bx) + abs(sy - by) } )

off_limit = set()
for zone in zones:
    if abs(zone['y'] - y_const) < zone['d']:
        delta_dist = abs(zone['y'] - y_const)
        flack = zone['d'] - delta_dist
        for i in range(-flack, flack + 1):
            off_limit.add(zone['x'] - i)

print(len(off_limit - beacons))