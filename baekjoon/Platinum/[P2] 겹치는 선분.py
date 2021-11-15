import sys
from collections import defaultdict
input = sys.stdin.readline

ans = 0
lines = defaultdict(list)

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        key = ('inf', x1)
        if y1 <= y2: x1, x2 = y1, y2
        else: x1, x2 = y2, y1
    else:
        a = (y2 - y1) / (x2 - x1)
        y0 = y1 - (a * x1)
        key = (round(a, 6), round(y0, 6))
        if x1 > x2: x1, x2 = x2, x1
    lines[key].append((x1, 1))
    lines[key].append((x2, -1))

for arr in lines.values():
    if len(arr) == 2: continue
    arr.sort()
    cur = 0
    for p in arr:
        if p[1] == 1: ans += cur
        cur += p[1]

print(ans)
