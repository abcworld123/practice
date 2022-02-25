import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def update(seg, lazy, s, e, l, r, i):
    propagation(seg, lazy, s, e, i)
    if e < l or r < s: return
    elif l <= s and e <= r:
        lazy[i] ^= 1
        propagation(seg, lazy, s, e, i)
    else:
        m, ch = (s + e) >> 1, i << 1
        update(seg, lazy, s, m, l, r, ch)
        update(seg, lazy, m + 1, e, l, r, ch + 1)
        seg[i] = seg[ch] + seg[ch + 1]

def propagation(seg, lazy, s, e, i):
    if lazy[i]:
        seg[i] = (recv[e + 1] - recv[s]) - seg[i]
        if s != e:
            ch = i << 1
            lazy[ch] ^= lazy[i]
            lazy[ch + 1] ^= lazy[i]
        lazy[i] = 0


N = int(input())
comp = set()
recv = [0] * 200001
qry = []

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    qry.append((y1, x1, x2))
    qry.append((y2, x1, x2))
    comp.add(x1)
    comp.add(x2)

comp = {v: i for i, v in enumerate(sorted(comp), start=1)}
for i, v in comp.items(): recv[v] = i
qry.sort(key=lambda x: x[0])

n = len(comp) - 1
seg = [0] * (1 << (n.bit_length() + 1))
lazy = seg[:]
cur, ans = 0, 0

for y, x1, x2 in qry:
    dy = y - cur
    cur = y
    ans += seg[1] * dy
    update(seg, lazy, 1, n, comp[x1], comp[x2] - 1, 1)

print(ans)
