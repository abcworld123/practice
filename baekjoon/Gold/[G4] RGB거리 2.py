import sys

N = int(input())
arr = [list(map(int, x.split())) for x in sys.stdin.readlines()]
ans = []

for c in range(3):
	dp = [[float('inf')] * 3]
	dp[0][c] = arr[0][c]
	for i in range(1, N):
		r, g, b = arr[i]
		dp.append([min(dp[-1][1], dp[-1][2]) + r, min(dp[-1][0], dp[-1][2]) + g, min(dp[-1][0], dp[-1][1]) + b])
	dp[-1][c] = float('inf')
	ans += dp[-1]

print(min(ans))

# 어려웠음
