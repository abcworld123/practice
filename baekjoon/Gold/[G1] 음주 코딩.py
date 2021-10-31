import sys
input = sys.stdin.readline

def init(segtree, start, end, i):
    if start == end: segtree[i] = arr[start]
    else:
        mid, child = (start + end) >> 1, i << 1
        segtree[i] = init(segtree, start, mid, child) * init(segtree, mid + 1, end, child + 1)
    return segtree[i]


def mul(segtree, start, end, left, right, i):
    if right < start or left > end: return 1
    if left <= start and end <= right: return segtree[i]
    mid, child = (start + end) >> 1, i << 1
    return mul(segtree, start, mid, left, right, child) * mul(segtree, mid + 1, end, left, right, child + 1)


def update(segtree, start, end, target, i, diff):
    child = i << 1
    if start != end:
        mid = (start + end) >> 1
        if target <= mid: update(segtree, start, mid, target, child, diff)
        else: update(segtree, mid + 1, end, target, child + 1, diff)
    if start == end: segtree[i] += diff
    else: segtree[i] = segtree[child] * segtree[child + 1]


lines = [*open(0)]
cur = 0

while cur < len(lines):
    N, K = map(int, lines[cur].split())
    arr = [0] + [x // abs(x) if x else 0 for x in map(int, lines[cur + 1].split())]
    segtree = [0] * (1 << (N.bit_length() + 1))
    init(segtree, 1, N, 1)

    for i in range(cur + 2, cur + 2 + K):
        op, a, b = lines[i].split()
        a, b = int(a), int(b)
        if op == 'C':
            if arr[a] * b > 0 or arr[a] == b: continue
            elif b == 0: diff = -arr[a] // abs(arr[a])
            elif arr[a] == 0: diff = b // abs(b)
            elif arr[a] > 0: diff = -2
            else: diff = 2
            update(segtree, 1, N, a, 1, diff)
            arr[a] = b
        else:
            val = mul(segtree, 1, N, a, b, 1)
            print(0 if val == 0 else '+' if val > 0 else '-', end='')
    cur += K + 2
    print()
