# aidan
# aoc2024 day23
#

lines = []

with open('input/day23.txt') as f:
    for line in f:
        lines.append(line.strip())

connections = {}

for line in lines:
    node1, node2 = tuple(line.split('-'))
    connections.setdefault(node1, {node1}).add(node2)
    connections.setdefault(node2, {node2}).add(node1)

res_set = set()
for og_node, og_node_connections in connections.items():
    nodes = [node for node in og_node_connections if node != og_node]
    for i, node_i in enumerate(nodes):
        for j, node_j in enumerate(nodes[i+1:]):
            if node_i in connections[node_j] and 't' in (og_node[0], node_i[0], node_j[0]):
                res_set.add(frozenset({og_node, node_i, node_j}))

# part 1
ans_p1 = len(res_set)
print(f"\nFirst Problem Solution: {ans_p1}")

res_set = set()
for og_node, og_node_connections in connections.items():
    nodes = {node for node in og_node_connections if node != og_node}
    frontier = [{node} for node in nodes]
    seen = set()
    while frontier:
        curr_set = frontier.pop(0)
        for node_hypo in nodes.difference(curr_set):
            flag = True
            for node_curr in curr_set:
                if node_hypo not in connections[node_curr]:
                    flag = False
                    break
            hypo_set = curr_set.union({node_hypo})
            if flag and frozenset(hypo_set) not in seen:
                frontier.append(hypo_set)
                seen.add(frozenset(hypo_set))
                if len(hypo_set) > len(res_set) - 1 : res_set = hypo_set.union({og_node})

# part 2
ans_p2 = ','.join(sorted(list(res_set)))
print(f"\nSecond Problem Solution: {ans_p2}\n")
