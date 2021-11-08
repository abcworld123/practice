import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = arr[start]
    else:
        mid, child = (start + end) >> 1, i << 1
        left = init(segtree, start, mid, child)
        right = init(segtree, mid + 1, end, child + 1)
        segtree[i] = min(left, right)
    return segtree[i]


def get(segtree, start, end, left, right, i):
    if left <= start and end <= right: return segtree[i]
    else:
        mid, child = (start + end) >> 1, i << 1
        arr = []
        if left <= mid: arr.append(get(segtree, start, mid, left, right, child))
        if mid + 1 <= right: arr.append(get(segtree, mid + 1, end, left, right, child + 1))
        return min(arr)


def update(segtree, start, end, target, i, val):
    if start == end:
        segtree[i] = val
    else:
        mid, child = (start + end) >> 1, i << 1
        if target <= mid: update(segtree, start, mid, target, child, val)
        else: update(segtree, mid + 1, end, target, child + 1, val)
        segtree[i] = min(segtree[child], segtree[child + 1])
    return segtree[i]


N = int(input())
arr = [0] + list(map(int, input().split()))
segtree = [0] * (1 << (N.bit_length() + 1))
init(segtree, 1, N, 1)

for i in range(int(input())):
    op, a, b = tuple(map(int, input().split()))
    if op == 1: update(segtree, 1, N, a, 1, b)
    else: print(get(segtree, 1, N, a, b, 1))
