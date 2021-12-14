import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
arr = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a <= N and b <= M: arr.append([b, a])
comp = {v: k for k, v in enumerate(sorted(set(y[1] for y in arr)), start=1)}
for y in arr: y[1] = comp[y[1]]
arr.sort()

n = len(comp)
seg = [0] * (2 * n)

for _, y in arr:
    cat, l, r = 0, n, n + y
    while l < r:
        if l & 1:
            if cat < seg[l]: cat = seg[l]
            l += 1
        if r & 1:
            r -= 1
            if cat < seg[r]: cat = seg[r]
        l >>= 1
        r >>= 1
    i, v = y + n - 1, cat + 1
    seg[i] = v
    while i > 1:
        seg[i >> 1] = seg[i] if seg[i] > seg[i ^ 1] else seg[i ^ 1]
        i >>= 1

print(seg[1] if seg else 0)
