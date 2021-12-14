import os, io, sys
from collections import defaultdict
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def init(seg, leaf, s, e, i):
    if s == e: seg[i] = 1; leaf[s - 1] = i
    else: seg[i] = init(seg, leaf, s, (s + e) >> 1, i << 1) + init(seg, leaf, ((s + e) >> 1) + 1, e, (i << 1) + 1)
    return seg[i]


N = int(input())
dic = defaultdict(list)
seg = [1] * (1 << ((N - 1).bit_length() + 1))
for i, x in enumerate(map(int, input().split())): dic[x].append(i)
leaf = [0] * (N)
ans = [0] * (N)
if N >= 2: init(seg, leaf, 1, N, 1)
prev, total = 1, 0

for x in sorted(dic):
    cur = dic[x]
    total += (x - prev) * seg[1]
    for i in range(len(cur) - 1, -1, -1):
        j, k = leaf[cur[i]], 1
        while j > 1:
            if j & 1:
                k += seg[j - 1]
            seg[j] -= 1
            j >>= 1
        seg[j] -= 1
        ans[cur[i]] = total + k
    prev = x + 1
    total += seg[1] + len(cur)

sys.stdout.write('\n'.join(map(str, ans)))
