import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = 1
    else:
        mid = (start + end) >> 1
        segtree[i] = init(segtree, start, mid, i << 1) + init(segtree, mid + 1, end, (i << 1) + 1)
    return segtree[i]


def get(segtree, start, end, i, target):
    while start != end:
        segtree[i] -= 1
        mid, child = (start + end) >> 1, i << 1
        if target <= segtree[child]:
            end = mid
            i = child
        else:
            start = mid + 1
            i = child + 1
            target -= segtree[child]
    segtree[i] -= 1
    return start


N = int(input())
arr = [0] + sorted([int(input()) for _ in range(N)])
segtree = [-1] * (1 << (N.bit_length() + 1))
init(segtree, 1, N, 1)
ans = []

for x in tuple(map(int, input().split()))[::-1]:
    ans.append(arr[get(segtree, 1, N, 1, x + 1)])

print(*ans[::-1])
