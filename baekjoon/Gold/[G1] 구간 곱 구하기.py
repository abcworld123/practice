import sys
input = sys.stdin.readline
x = 1000000007

def init(segtree, start, end, i):
    if start == end: segtree[i] = arr[start]
    else:
        mid, child = (start + end) >> 1, i << 1
        segtree[i] = init(segtree, start, mid, child) * init(segtree, mid + 1, end, child + 1) % x
    return segtree[i]


def mul(segtree, start, end, left, right, i):
    if right < start or left > end: return 1
    if left <= start and end <= right: return segtree[i]
    mid, child = (start + end) >> 1, i << 1
    return mul(segtree, start, mid, left, right, child) * mul(segtree, mid + 1, end, left, right, child + 1) % x


def update(segtree, start, end, target, i, diff):
    child = i << 1
    if start != end:
        mid = (start + end) >> 1
        if target <= mid: update(segtree, start, mid, target, child, diff)
        else: update(segtree, mid + 1, end, target, child + 1, diff)
    if start == end: segtree[i] += diff
    else: segtree[i] = segtree[child] * segtree[child + 1] % x


N, M, K = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]
segtree = [0] * (1 << (N.bit_length() + 1))
init(segtree, 1, N, 1)

for i in range(M + K):
    op, a, b = map(int, input().split())
    if op == 1:
        update(segtree, 1, N, a, 1, b - arr[a])
        arr[a] = b
    else:
        print(mul(segtree, 1, N, a, b, 1) % x)
