import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def summ(seg, lazy, s, e, l, r, i):
    if lazy[i]: propagation(seg, lazy, s, e, i)
    if r < s or l > e: return 0
    if l <= s and e <= r: return seg[i]
    m, ch = (s + e) >> 1, i << 1
    return summ(seg, lazy, s, m, l, r, ch) | summ(seg, lazy, m + 1, e, l, r, ch + 1)

def update(seg, lazy, s, e, l, r, i, v):
    if lazy[i]: propagation(seg, lazy, s, e, i)
    if e < l or r < s: return
    if s == e: seg[i] = v
    elif l <= s and e <= r:
        ch = i << 1
        seg[i] = v
        lazy[ch] = v
        lazy[ch + 1] = v
    else:
        m, ch = (s + e) >> 1, i << 1
        update(seg, lazy, s, m, l, r, ch, v)
        update(seg, lazy, m + 1, e, l, r, ch + 1, v)
        seg[i] = seg[ch] | seg[ch + 1]

def propagation(seg, lazy, s, e, i):
    ch = i << 1
    seg[i] = lazy[i]
    if s != e:
        lazy[ch] = lazy[i]
        lazy[ch + 1] = lazy[i]
    lazy[i] = 0


N, T, Q = map(int, input().split())
seg = [2] * (1 << ((N - 1).bit_length() + 1))
lazy = seg[:]
ans = __pypy__.builders.StringBuilder()

for i in range(Q):
    t, *q = input().split()
    q = list(map(int, q))
    if q[0] > q[1]: q[0], q[1] = q[1], q[0]
    if t == b'C': update(seg, lazy, 1, N, q[0], q[1], 1, 1 << q[2])
    else: ans.append(str(bin(summ(seg, lazy, 1, N, q[0], q[1], 1)).count('1')) + '\n')

os.write(1, ans.build().encode())
