import sys
input = sys.stdin.readline


def summ(seg, lazy, s, e, l, r, i):
    propagation(seg, lazy, s, e, i)
    if r < s or l > e: return 0
    if l <= s and e <= r: return seg[i]
    mid, child = (s + e) >> 1, i << 1
    return summ(seg, lazy, s, mid, l, r, child) + summ(seg, lazy, mid + 1, e, l, r, child + 1)


def update(seg, lazy, s, e, l, r, i, diff):
    propagation(seg, lazy, s, e, i)
    if e < l or r < s: return
    if s == e: seg[i] += diff
    elif l <= s and e <= r:
        child = i << 1
        seg[i] += (e - s + 1) * diff
        lazy[child] += diff
        lazy[child + 1] += diff
    else:
        mid, child = (s + e) >> 1, i << 1
        update(seg, lazy, s, mid, l, r, child, diff)
        update(seg, lazy, mid + 1, e, l, r, child + 1, diff)
        seg[i] = seg[child] + seg[child + 1]


def propagation(seg, lazy, s, e, i):
    if lazy[i]:
        child = i << 1
        seg[i] += (e - s + 1) * lazy[i]
        if s != e:
            lazy[child] += lazy[i]
            lazy[child + 1] += lazy[i]
        lazy[i] = 0


for case in range(int(input())):
    n, m = map(int, input().split())
    queries = [(0, *map(int, input().split())) for _ in range(n)]
    for i in range(m):
        x1, x2, y1, y2 = map(int, input().split())
        queries.append((1, x1, y1, y2))
        queries.append((-1, x2, y1, y2))
    queries.sort(key=lambda x: (x[1], -x[0]))

    N, count = 100000, 0
    segtree = [0] * (1 << (N.bit_length() + 1))
    lazy = segtree[:]

    for q in queries:
        if q[0]: update(segtree, lazy, 1, N, q[2], q[3], 1, q[0])
        else: count += summ(segtree, lazy, 1, N, q[2], q[2], 1)
    print(count)


# 펜윅 구간-점 버전 (2배정도 빠름)
import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    qq = [(0, *map(int, input().split())) for _ in range(n)]
    for i in range(m):
        x1, x2, y1, y2 = map(int, input().split())
        qq.append((1, x1, y1, y2))
        qq.append((-1, x2, y1, y2))
    qq.sort(key=lambda x: (x[1], -x[0]))
    N, ans = 100001, 0
    fw = [0] * (N + 1)

    for q in qq:
        if q[0]:
            i, j, x = q[2] + 1, q[3] + 2, q[0]
            while i <= N: fw[i] += x; i += i & -i
            while j <= N: fw[j] -= x; j += j & -j
        else:
            i = q[2] + 1
            while i: ans += fw[i]; i -= i & -i
    print(ans)
