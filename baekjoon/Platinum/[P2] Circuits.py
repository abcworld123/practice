import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def update(seg, lazy, s, e, l, r, i, v):
    if lazy[i]: propagation(seg, lazy, s, e, i)
    if e < l or r < s: return
    if s == e: seg[i] += v
    elif l <= s and e <= r:
        seg[i] += v
        lazy[i << 1] += v
        lazy[i << 1 | 1] += v
    else:
        m, ch = (s + e) >> 1, i << 1
        update(seg, lazy, s, m, l, r, ch, v)
        update(seg, lazy, m + 1, e, l, r, ch + 1, v)
        seg[i] = max(seg[ch], seg[ch + 1])

def propagation(seg, lazy, s, e, i):
    seg[i] += lazy[i]
    if s != e:
        lazy[i << 1] += lazy[i]
        lazy[i << 1 | 1] += lazy[i]
    lazy[i] = 0


N = int(input())
arr = []
comp = set()

for _ in range(N):
    _, y1, _, y2 = map(int, input().split())
    arr.append([y2, y1, True])
    arr.append([y1, y2, False])
    comp.add(y1)
    comp.add(y2)

comp = {v: i for i, v in enumerate(sorted(comp), start=1)}
n = len(comp)
for i in range(len(arr)):
    arr[i][0] = comp[arr[i][0]]
    arr[i][1] = comp[arr[i][1]]

arr.sort(key=lambda x: (x[0], -x[2]))
seg = [0] * (1 << ((n - 1).bit_length() + 1))
lazy = seg[:]
ans, cur = 0, 0
for y1, y2, f in arr:
    if f: update(seg, lazy, 1, n, y1, y2, 1, 1)

for y1, y2, f in arr:
    if f:
        cur += 1
        update(seg, lazy, 1, n, y1, y2, 1, -1)
        ans = max(ans, cur + seg[1])
    else:
        cur -= 1
        update(seg, lazy, 1, n, y2, y1, 1, 1)

print(ans)
