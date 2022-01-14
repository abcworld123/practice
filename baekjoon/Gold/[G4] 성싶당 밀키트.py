import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, G, K = map(int, input().split())
arr1, arr2 = [], []
for _ in range(N):
    S, L, O = map(int, input().split())
    if O: arr2.append((S, L))
    else: arr1.append((S, L))

K = max(0, len(arr2) - K)
l, r = 0, 2 * 10 ** 9 + 1
ans = 0

while l < r:
    m = (l + r) >> 1
    v1 = [x[0] * max(1, m - x[1]) for x in arr1]
    v2 = sorted([x[0] * max(1, m - x[1]) for x in arr2])
    if sum(v1) + sum(v2[:K]) <= G:
        ans = m
        l = m + 1
    else:
        r = m

print(ans)
