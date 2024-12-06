lines = []
with open('./day15/beacons.txt') as f:
    for line in f:
        s = line.strip()
        lines.append(s)

zones = []
beacons = set()
for line in lines:
    sx = int(line.split('x=')[1].split(',')[0])
    sy = int(line.split('y=')[1].split(':')[0])
    bx = int(line.split('x=')[2].split(',')[0])
    by = int(line.split('y=')[2].split(':')[0])
    zones.append( { 'x' : sx, 'y' : sy, 'd' : abs(sx - bx) + abs(sy - by) } )

ob_const = 4000000

points = set()
for zone in zones:
    for y in range(max(0, zone['y'] - zone['d']), min(ob_const, zone['y'] + zone['d'] + 1)):
        delta = zone['d'] - abs(zone['y'] - y)
        points.add((zone['x'] + delta + 1, y))
        points.add((zone['x'] - delta - 1, y))
    
    for x in range(max(0, zone['x'] - zone['d']), min(ob_const, zone['x'] + zone['d'] + 1)):
        delta = zone['d'] - abs(zone['x'] - x)
        points.add((x, zone['y'] + delta + 1))
        points.add((x, zone['y'] - delta - 1))

for point in points:
    if point[0] >= 0 and point[1] >= 0 and point[0] <= ob_const and point[1] <= ob_const:
        flag = True
        z_i = 0
        while flag and z_i < len(zones):
            zone = zones[z_i]
            if abs(point[0] - zone['x']) + abs(point[1] - zone['y']) <= zone['d']:
                flag = False
            z_i += 1
        if flag:
            print(point[0] * 4000000 + point[1])
            break