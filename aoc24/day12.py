# aidan
# aoc2024 day12
#

lines = []

with open('input/day12.txt') as f:
    for line in f:
        lines.append(line.strip())

garden = []

for line in lines:
    garden.append([])
    for plot in line:
        garden[-1].append(plot)

regioned = set()
region_map = {}
rev_region_map = {}
id_counter = 0

def establish_region(row_i, col_j):
    frontier = [(row_i, col_j)]
    seen = {(row_i, col_j)}
    plant_type = garden[row_i][col_j]
    global id_counter
    region_id = id_counter
    region_map[region_id] = []
    id_counter += 1
    while frontier:
        i, j = frontier.pop()
        if i < 0 or j < 0 : continue
        curr_plant_type = garden[i][j]
        if curr_plant_type != plant_type : continue
        region_map[region_id].append((i, j))
        rev_region_map[(i, j)] = region_id
        regioned.add((i, j))
        ops = (
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1)
        )
        for ia, ja in ops:
            if (ia, ja) in seen : continue
            try:
                _ = garden[ia][ja]
                frontier.append((ia, ja))
                seen.add((ia, ja))
            except:
                pass
    return

for row_i in range(len(garden)):
    for col_j in range(len(garden[0])):
        if len(regioned) == len(garden)*len(garden[0]) : break
        if (row_i, col_j) not in regioned : establish_region(row_i, col_j)
    if len(regioned) == len(garden)*len(garden[0]) : break

ans = 0
edge_map = {}
for region_id in region_map.keys():
    seen = set()
    area = len(region_map[region_id])
    perim = 0
    for plot in region_map[region_id]:
        i, j = plot
        edges = 0
        for op in (
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1)
        ):
            if op not in region_map[region_id]:
                perim += 1
                edge_map.setdefault(region_id, []).append((min(plot, op), max(plot, op)))
    ans += area * perim

# part 1
ans_p1 = ans
print(f"\nFirst Problem Solution: {ans_p1}")

ans = 0
for region_id in region_map.keys():
    edge_connections = {}
    for edge in edge_map[region_id]:
        node1, node2 = edge
        og = None
        og = node1 if node1 in region_map[region_id] else node2
        r1, c1 = node1
        r2, c2 = node2
        o1 = ((min((r1 + 1, c1), (r2 + 1, c2))), max((r1 + 1, c1), (r2 + 1, c2)))
        o2 = ((min((r1 - 1, c1), (r2 - 1, c2))), max((r1 - 1, c1), (r2 - 1, c2)))
        o3 = ((min((r1, c1 + 1), (r2, c2 + 1))), max((r1, c1 + 1), (r2, c2 + 1)))
        o4 = ((min((r1, c1 - 1), (r2, c2 - 1))), max((r1, c1 - 1), (r2, c2 - 1)))
        if c1 == c2 : ops = [o3, o4]
        else : ops = [o1, o2]
        for op in ops:
            opa, opb = op
            opog = opa if opa in region_map[region_id] else opb
            if op in edge_map[region_id] and (og[0] == opog[0] or og[1] == opog[1]):
                edge_connections.setdefault(edge, []).append(op)
    curr_set = {edge for edge in edge_map[region_id]}
    seen = set()
    edge_count = 0
    while curr_set:
        edge_count += 1
        curr_edge = curr_set.pop()
        frontier = [curr_edge]
        while frontier:
            fedge = frontier.pop()
            l = []
            if fedge in curr_set:
                curr_set.remove(fedge)
            if fedge in edge_connections:
                l = edge_connections[fedge]
            for li in l:
                if li[0][0] == curr_edge[0][0] or li[0][1] == curr_edge[0][1]:
                    if li in curr_set : curr_set.remove(li)
                    if li not in seen : frontier.append(li)
                seen.add(li)
    ans += len(region_map[region_id]) * edge_count

# part 2
ans_p2 = ans
print(f"\nSecond Problem Solution: {ans_p2}\n")
