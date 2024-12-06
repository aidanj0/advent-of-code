# aidan
# aoc2024 day03, rewritten 2024/12/03
#

import math

PRFX = 'mul('
STRT = 'do()'
STOP = "don't()"

txt = ""

with open('input/day03.txt') as f:
    for line in f:
        txt += line

txt_og = txt

ans_p1 = 0
while True:
    cand = txt.find(PRFX)
    if cand == -1 : break
    txt = txt[cand + len(PRFX):]
    next_cand = txt.find(PRFX) if txt.find(PRFX) != -1 else math.inf
    reqs = txt.find(',') < txt.find(')') and txt.find(')') < next_cand
    if reqs:
        chunk = txt[:txt.find(')')]
        flag = False
        for c in chunk:
            if c not in ',0123456789':
                flag = True
        if chunk[0] not in '0123456789' or chunk[-1] not in '0123456789' or flag or chunk.count(',') != 1:
            pass
        else:
            nums = chunk.split(',')
            ans_p1 += int(nums[0]) * int(nums[1])
print(f"\nFirst Problem Solution: {ans_p1}")

txt = txt_og

ans_p2 = 0
while True:
    cand = txt.find(PRFX)
    if cand == -1 : break
    reqs = False
    if txt.find(STOP) != -1 and txt.find(STOP) < cand:
        if txt.find(STRT) == -1 : break
        txt = txt[txt.find(STRT):]
    else:
        txt = txt[cand + len(PRFX):]
        next_cand = txt.find(PRFX) if txt.find(PRFX) != -1 else math.inf
        reqs = txt.find(',') < txt.find(')') and txt.find(')') < next_cand
    if reqs:
        chunk = txt[:txt.find(')')]
        flag = False
        for c in chunk:
            if c not in ',0123456789':
                flag = True
        if chunk[0] not in '0123456789' or chunk[-1] not in '0123456789' or flag or chunk.count(',') != 1:
            pass
        else:
            nums = chunk.split(',')
            ans_p2 += int(nums[0]) * int(nums[1])
print(f"\nSecond Problem Solution: {ans_p2}\n")