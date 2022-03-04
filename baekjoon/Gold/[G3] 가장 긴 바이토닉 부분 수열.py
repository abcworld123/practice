import sys
from bisect import bisect_left
input = sys.stdin.readline

def fill(cur, i):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        cur[i] = len(dp)
    else:
        j = bisect_left(dp, arr[i])
        dp[j] = arr[i]
        cur[i] = j + 1


N = int(input())
arr = list(map(int, input().split()))
up, down = [0] * N, [0] * N

dp = [float('inf')]
for i in range(N): fill(up, i)

dp = [float('inf')]
for i in range(N - 1, -1, -1): fill(down, i)

print(max(up[i] + down[i] - 1 for i in range(N)))
