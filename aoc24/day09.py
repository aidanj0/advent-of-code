# aidan
# aoc2024 day09
#

lines = []

with open('input/day09.txt') as f:
    for line in f:
        lines.append(line.strip())

line = lines[0]
disk = []
free_indices = []
data_indices = []

for i, c in enumerate(line):
    if i % 2 == 0:
        # file block of len c, id of i / 2
        file_block_len = int(c)
        file_block_id = i // 2
        for j in range(file_block_len):
            data_indices.append((len(disk), file_block_id))
            disk.append(file_block_id)
    else:
        # c block free
        free_space_len = int(c)
        for j in range(free_space_len):
            free_indices.append(len(disk))
            disk.append('.')

p1disk = [tok for tok in disk]
p1free_indices = [tok for tok in free_indices]
p1data_indices = [tok for tok in data_indices]

while True:
    if not p1free_indices or not p1data_indices : break
    first_free_index = p1free_indices.pop(0)
    last_data_index, last_data_id = p1data_indices.pop()
    if first_free_index >= last_data_index : break
    p1disk[first_free_index] = last_data_id
    p1disk[last_data_index] = '.'

checksum = 0

for i, c in enumerate(p1disk):
    if c == '.' : break
    checksum += i * c

# part 1
ans_p1 = checksum
print(f"\nFirst Problem Solution: {checksum}")

p2data_indices = []
p2free_indices = []
p2disk = []

for i, c in enumerate(line):
    if i % 2 == 0:
        # file block of len c, id of i / 2
        file_block_len = int(c)
        file_block_id = i // 2
        p2data_indices.append( (file_block_id, len(p2disk), file_block_len) )
        for j in range(file_block_len):
            p2disk.append(file_block_id)
    else:
        # c block free
        free_space_len = int(c)
        p2free_indices.append( (len(p2disk), free_space_len) )
        for j in range(free_space_len):
            p2disk.append('.')

for file_block_id, starting_index, file_block_len in reversed(p2data_indices):
    for i in range(len(p2free_indices)):
        free_starting_index, free_space_len = p2free_indices[i]
        if free_starting_index > starting_index : break
        if free_space_len >= file_block_len:
            for j in range(free_starting_index, free_starting_index + file_block_len):
                p2disk[j] = file_block_id
            for j in range(starting_index, starting_index + file_block_len):
                p2disk[j] = '.'
            free_starting_index += file_block_len
            free_space_len -= file_block_len
            if free_space_len:
                p2free_indices[i] = (free_starting_index, free_space_len)
            else:
                p2free_indices.pop(i)
            break

p2checksum = 0

for i, c in enumerate(p2disk):
    if c == '.' : continue
    p2checksum += i * c

# part 2
ans_p2 = p2checksum
print(f"\nSecond Problem Solution: {ans_p2}\n")
