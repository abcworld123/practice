import os, io, sys
from bisect import bisect_left
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lis = [float('inf')]
dp = [0] * N
arr.sort()

for i in range(len(arr)):
    x = arr[i][1]
    if lis[-1] < x:
        lis.append(x)
        dp[i] = len(lis) - 1
    else:
        idx = bisect_left(lis, x)
        lis[idx] = x
        dp[i] = idx

i, j = N - 1, len(lis) - 1
ans = [0] * (j + 1)
while j >= 0:
    if dp[i] == j:
        ans[j] = arr[i][0]
        j -= 1
    i -= 1

print(N - len(ans))
ans.append(-1)
i = 0
for j, _ in arr:
    if j != ans[i]: print(j)
    else: i += 1
