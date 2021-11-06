import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = [arr[start], start]
    else:
        mid, child = (start + end) >> 1, i << 1
        segtree[i] = min(init(segtree, start, mid, child), init(segtree, mid + 1, end, child + 1), key=lambda x: x[0])[:]
    return segtree[i]


def get(segtree, start, end, left, right, i):
    if right < start or left > end: return (9999999999, -1)
    if left <= start and end <= right: return segtree[i]
    mid, child = (start + end) >> 1, i << 1
    return min(get(segtree, start, mid, left, right, child), get(segtree, mid + 1, end, left, right, child + 1), key=lambda x: x[0])[:]


def update(segtree, start, end, target, i, diff):
    if start != end:
        mid, child = (start + end) >> 1, i << 1
        if target <= mid: segtree[i] = min(update(segtree, start, mid, target, child, diff), segtree[child + 1])[:]
        else: segtree[i] = min(update(segtree, mid + 1, end, target, child + 1, diff), segtree[child])[:]
        return segtree[i]
    else:
        segtree[i][0] += diff
        return segtree[i]


N = int(input())
arr = [0] + list(map(int, input().split()))
segtree = [0] * (1 << (N.bit_length() + 1))
init(segtree, 1, N, 1)

for i in range(int(input())):
    op, a, b = map(int, input().split())
    if op == 1:
        update(segtree, 1, N, a, 1, b - arr[a])
        arr[a] = b
    else:
        print(get(segtree, 1, N, a, b, 1)[1])
