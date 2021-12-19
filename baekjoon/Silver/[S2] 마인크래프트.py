import sys
from collections import Counter

B = int(input().split()[2])
can = Counter(map(int, sys.stdin.read().split()))
s, e = min(can), max(can)
can = sorted(can.items(), reverse=True)
ans = []

for i in range(s, e + 1):
    add, remove = 0, 0
    for y, n in can:
        if y > i: remove += (y - i) * n
        else: add += (i - y) * n
        if add > B + remove: break
    else:
        ans.append([add + 2 * remove, i])

print(*min(ans, key=lambda x: (x[0], -x[1])))
