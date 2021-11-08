import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = (arr[start], arr[start])
    else:
        mid, child = (start + end) >> 1, i << 1
        left = init(segtree, start, mid, child)
        right = init(segtree, mid + 1, end, child + 1)
        segtree[i] = (min(left[0], right[0]), max(left[1], right[1]))
    return segtree[i]


def get(segtree, start, end, left, right, i):
    if left <= start and end <= right: return segtree[i]
    else:
        mid, child = (start + end) >> 1, i << 1
        arr = ()
        if left <= mid: arr += get(segtree, start, mid, left, right, child)
        if mid + 1 <= right: arr += get(segtree, mid + 1, end, left, right, child + 1)
        return min(arr), max(arr)


N, Q = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]
segtree = [0] * (1 << (N.bit_length() + 1))
init(segtree, 1, N, 1)

for i in range(Q):
    a, b = map(int, input().split())
    res = get(segtree, 1, N, a, b, 1)
    print(res[1] - res[0])
