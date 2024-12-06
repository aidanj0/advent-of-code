with open('./day08/treehouse.txt') as f:
    best = -1
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
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tile = matrix[i][j]
            if i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1:
                pass
            else:
                to_consider = [ matrix[i][:j][::-1], matrix[i][j + 1:], transpose[j][:i][::-1], transpose[j][i + 1:] ]
                product = 1
                for l in to_consider:
                    l = l[:-1]
                    incre = 1
                    for item in l:
                        if item < tile:
                            incre += 1
                        else : break
                    product *= incre
                best = max(best, product)
    print(best)