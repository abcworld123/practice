import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = arr[start]
    else:
        mid, child = (start + end) >> 1, i << 1
        segtree[i] = init(segtree, start, mid, child) + init(segtree, mid + 1, end, child + 1)
    return segtree[i]


def get(segtree, lazy, start, end, target, i):
    propagation(segtree, lazy, start, end, i)
    if start == end: return segtree[i]
    mid, child = (start + end) >> 1, i << 1
    if target <= mid: return get(segtree, lazy, start, mid, target, child)
    else: return get(segtree, lazy, mid + 1, end, target, child + 1)


def update(segtree, lazy, start, end, left, right, i, diff):
    propagation(segtree, lazy, start, end, i)
    if end < left or right < start: return
    if start == end: segtree[i] += diff
    elif left <= start and end <= right:
        child = i << 1
        segtree[i] += (end - start + 1) * diff
        lazy[child] += diff
        lazy[child + 1] += diff
    else:
        mid, child = (start + end) >> 1, i << 1
        update(segtree, lazy, start, mid, left, right, child, diff)
        update(segtree, lazy, mid + 1, end, left, right, child + 1, diff)
        segtree[i] = segtree[child] + segtree[child + 1]


def propagation(segtree, lazy, start, end, i):
    if lazy[i]:
        child = i << 1
        segtree[i] += (end - start + 1) * lazy[i]
        if start != end:
            lazy[child] += lazy[i]
            lazy[child + 1] += lazy[i]
        lazy[i] = 0


N = int(input())
arr = [0] + [*map(int, input().split())]
segtree = [0] * (1 << (N.bit_length() + 1))
lazy = segtree[:]
init(segtree, 1, N, 1)

for i in range(int(input())):
    line = list(map(int, input().split()))
    if line[0] == 1: update(segtree, lazy, 1, N, line[1], line[2], 1, line[3])
    else: print(get(segtree, lazy, 1, N, line[1], 1))
