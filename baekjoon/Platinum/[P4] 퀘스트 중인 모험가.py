import os, io
from bisect import bisect_left, bisect_right
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def init(seg):
    for i in range(n - 1, 0, -1):
        seg[i] = seg[i << 1] + seg[i << 1 | 1]

def query(seg, l, r):
    ret = 0
    while l < r:
        if l & 1:
            ret += seg[l]
            l += 1
        if r & 1:
            r -= 1
            ret += seg[r]
        l >>= 1
        r >>= 1
    return ret

def update(seg, i):
    seg[i] = 1
    while i > 1:
        seg[i >> 1] = seg[i] + seg[i ^ 1]
        i >>= 1


input()
ok = list(map(int, input().split()))
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
ps = set(ok)
ans = []

for x in arr:
    if x[0] == 1:
        ps.add(x[1])

ps = sorted(ps)
p = {x: i for i, x in enumerate(ps, start=1)}
n = len(ps)

seg = [0] * (2 * n)
for x in ok: seg[n + p[x] - 1] = 1
init(seg)

for x in arr:
    if x[0] == 1:
        update(seg, p[x[1]] + n - 1)
    else:
        l, r = bisect_left(ps, x[1]) + 1, bisect_right(ps, x[2])
        ans.append(x[2] - x[1] + 1 - query(seg, l + n - 1, r + n))

print('\n'.join(map(str, ans)))
