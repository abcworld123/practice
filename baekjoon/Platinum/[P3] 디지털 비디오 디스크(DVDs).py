import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
INF = [2 ** 20, -2 ** 20]
YES, NO = 'YES\n', 'NO\n'

def init(seg, leaf, s, e, i):
    if s == e:
        seg[i] = [s, s]
        leaf[s] = i
    else:
        m, ch = (s + e) >> 1, i << 1
        L = init(seg, leaf, s, m, ch)
        R = init(seg, leaf, m + 1, e, ch + 1)
        seg[i] = [L[0] if L[0] < R[0] else R[0], L[1] if L[1] > R[1] else R[1]]
    return seg[i]

def get_minmax(seg, s, e, l, r, i):
    if l <= s and e <= r: return seg[i]
    m, ch = (s + e) >> 1, i << 1
    L = get_minmax(seg, s, m, l, r, ch) if l <= m else INF
    R = get_minmax(seg, m + 1, e, l, r, ch + 1) if m + 1 <= r else INF
    return [L[0] if L[0] < R[0] else R[0], L[1] if L[1] > R[1] else R[1]]

def update_val(seg, i, v):
    seg[i] = [v, v]
    i >>= 1
    while i:
        ch = i << 1
        seg[i][0] = seg[ch][0] if seg[ch][0] < seg[ch + 1][0] else seg[ch + 1][0]
        seg[i][1] = seg[ch][1] if seg[ch][1] > seg[ch + 1][1] else seg[ch + 1][1]
        i >>= 1

def main():
    N, M = map(int, input().split())
    ans = __pypy__.builders.StringBuilder()
    seg = [0] * (1 << ((N - 1).bit_length() + 1))
    leaf = [0] * (N + 1)
    init(seg, leaf, 1, N, 1)

    for i in range(M):
        op, a, b = map(int, input().split())
        a, b = a + 1, b + 1
        if op == 0:
            A, B = seg[leaf[a]][0], seg[leaf[b]][0]
            update_val(seg, leaf[a], B)
            update_val(seg, leaf[b], A)
        else:
            l, r = get_minmax(seg, 1, N, a, b, 1)
            if l == a and r == b: ans.append(YES)
            else: ans.append(NO)

    os.write(1, ans.build().encode())


for T in range(int(input())): main()
