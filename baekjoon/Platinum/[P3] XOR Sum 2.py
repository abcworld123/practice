import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def init(leaf, s, e, i):
    if s == e: leaf[s] = i
    else:
        m, ch = (s + e) >> 1, i << 1
        init(leaf, s, m, ch)
        init(leaf, m + 1, e, ch + 1)

def xor(seg, s, e, i, k):
    ret = 0
    while s != e:
        m, ch = (s + e) >> 1, i << 1
        if k >= seg[ch + 1][1]:
            k -= seg[ch + 1][1]
            ret ^= seg[ch + 1][0]
            if k == 0: return ret
            e = m
            i = ch
        else:
            s = m + 1
            i = ch + 1
    if k & 1: ret ^= recv[s]
    return ret

def update(seg, i, v):
    while i:
        seg[i][0] ^= v
        seg[i][1] += 1
        i >>= 1


for _ in range(int(input())):
    Q = int(input())
    qry = [input().split() for _ in range(Q)]
    comp = set()
    for i in range(Q):
        qry[i][1] = int(qry[i][1])
        if qry[i][0][0] == 105: comp.add(qry[i][1])
    comp = {v: i for i, v in enumerate(sorted(comp), start=1)}
    n = len(comp)
    recv = [0] * (n + 1)
    for i, v in comp.items(): recv[v] = i
    ans = []

    seg = [[0, 0] for _ in range(1 << ((n - 1).bit_length() + 1))]
    leaf = [0] * (n + 1)
    init(leaf, 1, n, 1)

    for cmd, x in qry:
        if cmd[0] == 105:
            update(seg, leaf[comp[x]], x)
        else:
            if x >= seg[1][1]: ans.append(seg[1][0])
            else: ans.append(xor(seg, 1, n, 1, x))

    print('\n'.join(map(str, ans)))
