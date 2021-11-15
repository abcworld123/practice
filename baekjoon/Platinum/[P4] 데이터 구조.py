import sys
input = sys.stdin.readline

def get(segtree, start, end, k, i):
    while start != end:
        segtree[i] -= 1
        mid, child = (start + end) >> 1, i << 1
        if k <= segtree[child]:
            end = mid
            i = child
        else:
            start = mid + 1
            k -= segtree[child]
            i = child + 1
    segtree[i] -= 1
    return start

def update(segtree, start, end, target, i):
    while start != end:
        segtree[i] += 1
        mid, child = (start + end) >> 1, i << 1
        if target <= mid:
            end = mid
            i = child
        else:
            start = mid + 1
            i = child + 1
    segtree[i] += 1


N = 2000000
segtree = [0] * (1 << (N.bit_length() + 1))

for i in range(int(input())):
    op, x = map(int, input().split())
    if op == 1: update(segtree, 1, N, x, 1)
    else: print(get(segtree, 1, N, x, 1))
