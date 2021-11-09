import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = [arr[start], 0]
    else:
        mid, child = (start + end) >> 1, i << 1
        segtree[i] = find_fs(init(segtree, start, mid, child), init(segtree, mid + 1, end, child + 1))
    return segtree[i]


def find_fs(lc, rc):
    l, r, node = 0, 0, []
    for _ in range(2):
        if lc[l] >= rc[r]: node.append(lc[l]); l += 1
        else: node.append(rc[r]); r += 1
    return node


def get(segtree, start, end, left, right, i):
    if left <= start and end <= right: return segtree[i]
    mid, child = (start + end) >> 1, i << 1
    if mid < left: return get(segtree, mid + 1, end, left, right, child + 1)
    elif mid + 1 > right: return get(segtree, start, mid, left, right, child)
    else: return find_fs(get(segtree, start, mid, left, right, child), get(segtree, mid + 1, end, left, right, child + 1))


def update(segtree, start, end, target, i, val):
    if start == end: segtree[i][0] = val
    else:
        mid, child = (start + end) >> 1, i << 1
        if target <= mid: segtree[i] = find_fs(update(segtree, start, mid, target, child, val), segtree[child + 1])
        else: segtree[i] = find_fs(segtree[child], update(segtree, mid + 1, end, target, child + 1, val))
    return segtree[i]


N = int(input())
arr = [0] + list(map(int, input().split()))
segtree = [0] * (1 << (N.bit_length() + 1))
init(segtree, 1, N, 1)

for i in range(int(input())):
    op, a, b = map(int, input().split())
    if op == 1: update(segtree, 1, N, a, 1, b)
    else: print(sum(get(segtree, 1, N, a, b, 1)))
