import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(input())
sss = lambda t: int(t[:2]) * 3600000 + int(t[3:5]) * 60000 + int(t[6:8]) * 1000 + int(t[9:])
arr = []
for _ in range(N):
    a, b = input().split()
    arr.append((sss(a), 1))
    arr.append((sss(b), -1))
arr.sort()
ans, cur = 0, 0

for _, x in arr:
    cur += x
    if ans < cur: ans = cur
print(ans)
