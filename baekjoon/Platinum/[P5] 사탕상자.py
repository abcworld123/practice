import sys
input = sys.stdin.readline


def pop(segtree, start, end, rank, i):
    while start != end:
        segtree[i] -= 1
        mid, child = (start + end) >> 1, i << 1
        if rank <= segtree[child]:
            end = mid
            i = child
        else:
            start = mid + 1
            rank -= segtree[child]
            i = child + 1
    segtree[i] -= 1
    return start


def update(segtree, start, end, target, i, diff):
    while start != end:
        segtree[i] += diff
        mid, child = (start + end) >> 1, i << 1
        if target <= mid:
            end = mid
            i = child
        else:
            start = mid + 1
            i = child + 1
    segtree[i] += diff


n = int(input())
taste = 1000000
arr = [0] * (taste + 1)
segtree = [0] * (1 << (taste.bit_length() + 1))

for i in range(1, n + 1):
    x = tuple(map(int, input().split()))
    if x[0] == 2:
        update(segtree, 1, taste, x[1], 1, x[2])
        arr[x[1]] += x[2]
    else:
        print(pop(segtree, 1, taste, x[1], 1))
