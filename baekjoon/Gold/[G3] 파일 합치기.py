import sys
input = sys.stdin.buffer.readline

for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * i for i in range(1, N + 1)]

    lens = arr[:] + [0]
    for i in range(1, N): lens[i] += lens[i - 1]

    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            print(j, i)
            dp[i][j] = min(dp[k][j] + dp[i][k + 1] + lens[i] - lens[j - 1] for k in range(j, i))

    print(dp[-1][0])
