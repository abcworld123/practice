import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

inf = 2 ** 20
inf2 = [inf, -inf]

def init(seg, leaf, s, e, i):
    if s == e:
        seg[i] = [idx[s], arr[s], arr[s]]
        leaf[s] = i
    else:
        m, ch = (s + e) >> 1, i << 1
        L = init(seg, leaf, s, m, ch)
        R = init(seg, leaf, m + 1, e, ch + 1)
        seg[i] = [L[0] if L[0] < R[0] else R[0], L[1] if L[1] < R[1] else R[1], L[2] if L[2] > R[2] else R[2]]
    return seg[i]

def get_idx(seg, s, e, l, r, i):
    if r < s or l > e: return inf
    if l <= s and e <= r: return seg[i][0]
    m, ch = (s + e) >> 1, i << 1
    return min(get_idx(seg, s, m, l, r, ch), get_idx(seg, m + 1, e, l, r, ch + 1))

def get_minmax(seg, s, e, l, r, i):
    if r < s or l > e: return inf2
    if l <= s and e <= r: return [seg[i][1], seg[i][2]]
    m, ch = (s + e) >> 1, i << 1
    L = get_minmax(seg, s, m, l, r, ch)
    R = get_minmax(seg, m + 1, e, l, r, ch + 1)
    return [L[0] if L[0] < R[0] else R[0], L[1] if L[1] > R[1] else R[1]]

def update_idx(seg, i, v):
    seg[i][0] = v
    i >>= 1
    while i:
        ch = i << 1
        seg[i][0] = seg[ch][0] if seg[ch][0] < seg[ch + 1][0] else seg[ch + 1][0]
        i >>= 1

def update_val(seg, i, v):
    seg[i][1] = v
    seg[i][2] = v
    i >>= 1
    while i:
        ch = i << 1
        seg[i][1] = seg[ch][1] if seg[ch][1] < seg[ch + 1][1] else seg[ch + 1][1]
        seg[i][2] = seg[ch][2] if seg[ch][2] > seg[ch + 1][2] else seg[ch + 1][2]
        i >>= 1


N, M = map(int, input().split())
idx = [0] * (N + 1)
arr = [0] + list(map(int, input().split()))
ans = __pypy__.builders.StringBuilder()
for i in range(len(arr)): idx[arr[i]] = i
seg = [0] * (1 << ((N - 1).bit_length() + 1))
leaf = [0] * (N + 1)
init(seg, leaf, 1, N, 1)

for i in range(M):
    op, a, b = map(int, input().split())
    if op == 1:
        A, B = seg[leaf[a]][1], seg[leaf[b]][1]
        update_idx(seg, leaf[A], b)
        update_idx(seg, leaf[B], a)
        update_val(seg, leaf[a], B)
        update_val(seg, leaf[b], A)
    else:
        s = get_idx(seg, 1, N, a, b, 1)
        l, r = get_minmax(seg, 1, N, s, s + b - a, 1)
        if l == a and r == b: ans.append('YES\n')
        else: ans.append('NO\n')

os.write(1, ans.build().encode())
