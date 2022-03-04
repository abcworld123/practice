N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]
arr[0][0] = 1000000

flag = 1
for i in range(1, M):
    arr[0][i] = arr[0][i - 1] + i * flag
    flag *= -1

flag_i = 1
cur = M
for i in range(1, N):
    flag = flag_i
    for j in range(M):
        arr[i][j] = arr[i - 1][j] + cur * flag
        flag *= -1
        cur += 1
    flag_i *= -1
    cur += M - 1

print('\n'.join(' '.join(map(str, line)) for line in arr))
