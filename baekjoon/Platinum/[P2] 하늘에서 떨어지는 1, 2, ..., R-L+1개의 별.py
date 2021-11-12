import sys
input = sys.stdin.readline


def init(seg, s, e, i):
    if s == e: seg[i] = arr[s]
    else:
        mid, child = (s + e) >> 1, i << 1
        seg[i] = init(seg, s, mid, child) + init(seg, mid + 1, e, child + 1)
    return seg[i]


def get(seg, lazy, lazy2, s, e, l, r, i, L):
    if lazy[i]: propagation(seg, lazy, lazy2, s, e, i)
    if r < s or l > e: return 0
    if l <= s and e <= r: return seg[i]
    mid, child = (s + e) >> 1, i << 1
    if l <= mid: return get(seg, lazy, lazy2, s, mid, l, r, child, L)
    else: return get(seg, lazy, lazy2, mid + 1, e, l, r, child + 1, L)


def update(seg, lazy, lazy2, s, e, l, r, i, L):  # L: left_blank
    if lazy[i]: propagation(seg, lazy, lazy2, s, e, i)
    if s == e: seg[i] += s - L
    elif l <= s and e <= r:
        lazy[i] = s - L
        lazy2[i] = 1
    else:
        mid, child = (s + e) >> 1, i << 1
        if l <= mid: update(seg, lazy, lazy2, s, mid, l, r, child, L)
        if mid + 1 <= r: update(seg, lazy, lazy2, mid + 1, e, l, r, child + 1, L)
        a, b = max(s, l) - L, min(e, r) - L
        seg[i] += (a + b) * (b - a + 1) // 2

def propagation(seg, lazy, lazy2, s, e, i):
    child = i << 1
    seg[i] += (2 * lazy[i] + lazy2[i] * (e - s)) * (e - s + 1) // 2
    if s != e:
        lazy[child] += lazy[i]
        lazy[child + 1] += lazy[i] + lazy2[i] * ((e - s + 2) // 2)
        lazy2[child] += lazy2[i]
        lazy2[child + 1] += lazy2[i]
    lazy[i] = 0
    lazy2[i] = 0


N = int(input())
arr = [0] + list(map(int, input().split()))
segtree = [0] * (1 << (N.bit_length() + 1))
lazy, lazy2 = segtree[:], segtree[:]
init(segtree, 1, N, 1)
for i in range(int(input())):
    line = list(map(int, input().split()))
    if line[0] == 1: update(segtree, lazy, lazy2, 1, N, line[1], line[2], 1, line[1] - 1)
    else: print(get(segtree, lazy, lazy2, 1, N, line[1], line[1], 1, line[1] - 1))
