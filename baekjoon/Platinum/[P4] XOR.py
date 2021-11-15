import sys
input = sys.stdin.readline


def init(seg, s, e, i):
    if s == e: seg[i] = arr[s]
    else:
        mid = (s + e) >> 1
        seg[i] = init(seg, s, mid, i << 1) + init(seg, mid + 1, e, (i << 1) + 1)
    return seg[i]


def summ(seg, lazy, s, e, target, i):
    propagation(seg, lazy, s, e, i)
    if s == e: return seg[i]
    mid = (s + e) >> 1
    if target <= mid: return summ(seg, lazy, s, mid, target, i << 1)
    else: return summ(seg, lazy, mid + 1, e, target, (i << 1) + 1)


def update(seg, lazy, s, e, l, r, i, x):
    propagation(seg, lazy, s, e, i)
    if s == e: seg[i] ^= x
    elif l <= s and e <= r:
        seg[i] ^= x
        lazy[i << 1] ^= x
        lazy[(i << 1) + 1] ^= x
    else:
        mid = (s + e) >> 1
        if l <= mid: update(seg, lazy, s, mid, l, r, i << 1, x)
        if mid + 1 <= r: update(seg, lazy, mid + 1, e, l, r, (i << 1) + 1, x)
        seg[i] = seg[i << 1] + seg[(i << 1) + 1]


def propagation(seg, lazy, s, e, i):
    if lazy[i]:
        seg[i] ^= lazy[i]
        if s != e:
            lazy[i << 1] ^= lazy[i]
            lazy[(i << 1) + 1] ^= lazy[i]
        lazy[i] = 0


n = int(input())
arr = [0] + list(map(int, input().split()))
seg = [0] * (1 << (n.bit_length() + 1))
lazy = seg[:]
init(seg, 1, n, 1)

m = int(input())
for i in range(m):
    line = list(map(int, input().split()))
    if line[0] == 1: update(seg, lazy, 1, n, line[1] + 1, line[2] + 1, 1, line[3])
    else: print(summ(seg, lazy, 1, n, line[1] + 1, 1))
