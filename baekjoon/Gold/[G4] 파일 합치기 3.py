import os, io
from heapq import *
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

ans = []

for T in range(int(input())):
    N = int(input())
    hq = list(map(int, input().split()))
    heapify(hq)
    cur = 0

    for _ in range(N - 1):
        x = heappop(hq) + heappop(hq)
        cur += x
        heappush(hq, x)

    ans.append(cur)

print('\n'.join(map(str, ans)))
