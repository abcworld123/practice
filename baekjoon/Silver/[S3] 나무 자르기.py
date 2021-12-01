import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
arr = tuple(map(int, input().split()))
l, r = 1, max(arr)
m = (l + r) >> 1
ans = 0

while l <= r:
    m = (l + r) >> 1
    total = sum((x - m for x in arr if x > m))
    if total >= M: ans = max(ans, m); l = m + 1
    else: r = m - 1

print(ans)
