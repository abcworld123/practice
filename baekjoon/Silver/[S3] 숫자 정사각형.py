N, M = map(int, input().split())
arr = [input() for _ in range(N)]
min_nm = min(N, M)

for i in range(min_nm - 1, 0, -1):
    for r in range(N - i):
        for c in range(M - i):
            if arr[r][c] == arr[r][c + i] == arr[r + i][c] == arr[r + i][c + i]:
                print((i + 1) ** 2)
                exit()
print(1)
