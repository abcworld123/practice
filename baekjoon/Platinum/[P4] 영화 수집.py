import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def init(seg, leaf, s, e, i, M):
    if s == e:
        if M < s: seg[i] = 1
        leaf[s] = i
    else:
        m, ch = (s + e) >> 1, i << 1
        seg[i] = init(seg, leaf, s, m, ch, M) + init(seg, leaf, m + 1, e, ch + 1, M)
    return seg[i]

def summ(seg, s, e, l, r, i):
    if l <= s and e <= r: return seg[i]
    m, ch = (s + e) >> 1, i << 1
    return (summ(seg, s, m, l, r, ch) if l <= m else 0) + (summ(seg, m + 1, e, l, r, ch + 1) if m + 1 <= r else 0)


ans = __pypy__.builders.StringBuilder()

for T in range(int(input())):
    N, M = map(int, input().split())
    pop = list(map(int, input().split()))
    seg = [0] * (1 << ((M + N - 1).bit_length() + 1))
    idx = list(range(M, M + N + 1))
    leaf = [0] * (N + M + 1)
    init(seg, leaf, 1, N + M, 1, M)

    for i in range(M):
        l, r = leaf[M - i], leaf[idx[pop[i]]]
        ans.append(str(summ(seg, 1, N + M, 1, idx[pop[i]] - 1, 1)) + ' ')
        while l: seg[l] += 1; l >>= 1
        while r: seg[r] -= 1; r >>= 1
        idx[pop[i]] = M - i

    ans.append('\n')

os.write(1, ans.build().encode())
