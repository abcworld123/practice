k, n = map(int, input().split())
dp = [[0] * 128 for _ in range(n)]
dp[0] = [0] + [1] + [2] * 126

for i in range(1, n):
    for j in range(1, 127):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(dp[n - 1][k])
