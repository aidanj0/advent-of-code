with open('./day08/treehouse.txt') as f:
    lines = []
    for line in f:
        s = line.strip()
        lines.append(s)
    matrix = []
    for line in lines:
        row = []
        for c in line:
            row.append(int(c))
        matrix.append(row)
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tile = matrix[i][j]
            if i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1:
                count += 1
            else:
                to_consider = [ matrix[i][:j], matrix[i][j + 1:], transpose[j][:i], transpose[j][i + 1:] ]
                for l in to_consider:
                    if sum([0 if tile > other_tile else 1 for other_tile in l] + [0]) == 0:
                        count += 1
                        break
    print(count)