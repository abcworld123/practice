def pop(segtree, start, end, rank, i):
    if start != end:
        mid, child = (start + end) >> 1, i << 1
        if rank <= segtree[child]:
            return pop(segtree, start, mid, rank, child)
        else:
            return pop(segtree, mid + 1, end, rank - segtree[child], child + 1)
    else:
        update(segtree, 1, taste, start, 1, -1)
        return start


def update(segtree, start, end, target, i, diff):
    segtree[i] += diff
    if start != end:
        mid, child = (start + end) >> 1, i << 1
        if target <= mid:
            update(segtree, start, mid, target, child, diff)
        else:
            update(segtree, mid + 1, end, target, child + 1, diff)


stdin = [*open(0)]
n = int(stdin[0])
taste = 1000000
arr = [0] * (taste + 1)
segtree = [0] * (1 << (taste.bit_length() + 1))

for i in range(1, n + 1):
    x = tuple(map(int, stdin[i].split()))
    if x[0] == 2:
        update(segtree, 1, taste, x[1], 1, x[2])
        arr[x[1]] += x[2]
    else:
        print(pop(segtree, 1, taste, x[1], 1))
