N = int(input())
dp = [[1] * 10 for _ in range(N)]

for i in range(1, N):
    s = sum(dp[i - 1])
    for j in range(10):
        dp[i][j] = s
        s -= dp[i - 1][j]

print(sum(dp[-1]) % 10007)
