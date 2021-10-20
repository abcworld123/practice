import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = arr[start]
    else:
        mid, child = (start + end) >> 1, i << 1
        segtree[i] = init(segtree, start, mid, child) + init(segtree, mid + 1, end, child + 1)
    return segtree[i]


def summ(segtree, lazy, start, end, left, right, i):
    propagation(segtree, lazy, start, end, i)
    if right < start or left > end: return 0
    if left <= start and end <= right: return segtree[i]
    mid, child = (start + end) >> 1, i << 1
    return summ(segtree, lazy, start, mid, left, right, child) + summ(segtree, lazy, mid + 1, end, left, right, child + 1)


def update(segtree, lazy, start, end, left, right, i, diff):
    propagation(segtree, lazy, start, end, i)
    if end < left or right < start: return
    elif left <= start and end <= right:
        lazy[i] ^= 1
        propagation(segtree, lazy, start, end, i)
    else:
        mid, child = (start + end) >> 1, i << 1
        update(segtree, lazy, start, mid, left, right, child, diff)
        update(segtree, lazy, mid + 1, end, left, right, child + 1, diff)
        segtree[i] = segtree[child] + segtree[child + 1]


def propagation(segtree, lazy, start, end, i):
    if lazy[i]:
        child = i << 1
        segtree[i] = (end - start + 1) - segtree[i]
        if start != end:
            lazy[child] ^= lazy[i]
            lazy[child + 1] ^= lazy[i]
        lazy[i] = 0


N, M = map(int, input().split())
arr = [0] * (N + 1)
segtree = [0] * (1 << (N.bit_length() + 1))
lazy = segtree[:]
init(segtree, 1, N, 1)

for i in range(M):
    line = list(map(int, input().split()))
    if line[0] == 0: update(segtree, lazy, 1, N, line[1], line[2], 1, 1)
    else: print(summ(segtree, lazy, 1, N, line[1], line[2], 1))
