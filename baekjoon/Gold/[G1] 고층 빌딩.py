N, L, R = map(int, input().split())
arr = [[[0 for _ in range(R + 1)] for _ in range(L + 1)] for _ in range(N)]
arr[0][0][0] = 1

for i in range(1, N):
    for j in range(L):
        for k in range(R):
            arr[i][j][k] = (arr[i - 1][j - 1][k] + arr[i - 1][j][k - 1] + arr[i - 1][j][k] * (i - 1)) % 1000000007

print(arr[N-1][L-1][R-1])
