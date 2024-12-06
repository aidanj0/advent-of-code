import heapq as hq

with open('./day01/calories.txt') as f:
    heap = []
    curr = 0
    for line in f:
        s = line.strip()
        if s:
            curr += int(s)
        else:
            if len(heap) == 3:
                hq.heappushpop(heap, curr)
            else:
                hq.heappush(heap, curr)
            curr = 0
    print(sum(heap)) # 206104