import sys
input = sys.stdin.readline


def init(segtree, start, end, i):
    if start == end: segtree[i] = 1
    else:
        mid, child = (start + end) >> 1, i << 1
        segtree[i] = init(segtree, start, mid, child) + init(segtree, mid + 1, end, child + 1)
    return segtree[i]


def get(segtree, start, end, i, target):
    segtree[i] -= 1
    if start == end: return start
    mid, child = (start + end) >> 1, i << 1
    if target <= segtree[child]: return get(segtree, start, mid, child, target)
    else: return get(segtree, mid + 1, end, child + 1, target - segtree[child])


N = int(input())
arr = [0] + sorted([int(input()) for _ in range(N)])
segtree = [-1] * (1 << (N.bit_length() + 1))
init(segtree, 1, N, 1)
ans = []

for x in tuple(map(int, input().split()))[::-1]:
    ans.append(arr[get(segtree, 1, N, 1, x + 1)])

print(*ans[::-1])
