dp = [[0] * 100 for _ in range(100)]
for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    dp[a - 1][b - 1] = 1

for j in range(2, 100):
    for i in range(100 - j):
        dp[i][i + j] += max(dp[i][k] + dp[k + 1][i + j] for k in range(i, i + j))

print(dp[0][99])
