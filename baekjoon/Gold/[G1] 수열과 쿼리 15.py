import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = (arr[start], start)
    else:
        mid, child = (start + end) >> 1, i << 1
        left = init(segtree, start, mid, child)
        right = init(segtree, mid + 1, end, child + 1)
        segtree[i] = min(left, right, key=lambda x: x[0])[:]
    return segtree[i]


def update(segtree, start, end, target, i, val):
    if start == end:
        segtree[i] = (val, target)
    else:
        mid, child = (start + end) >> 1, i << 1
        if target <= mid: update(segtree, start, mid, target, child, val)
        else: update(segtree, mid + 1, end, target, child + 1, val)
        segtree[i] = min(segtree[child], segtree[child + 1], key=lambda x: x[0])
    return segtree[i]


N = int(input())
arr = [0] + list(map(int, input().split()))
segtree = [0] * (1 << (N.bit_length() + 1))
init(segtree, 1, N, 1)

for i in range(int(input())):
    lines = tuple(map(int, input().split()))
    if lines[0] == 1: update(segtree, 1, N, lines[1], 1, lines[2])
    else: print(segtree[1][1])
