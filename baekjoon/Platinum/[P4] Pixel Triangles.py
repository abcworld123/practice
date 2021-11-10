import sys
input = sys.stdin.readline

N = 2001
arr = [[0] * N for _ in range(N)]
ans = 0

for i in range(int(input())):
    a, b, c = map(int, input().split())
    if arr[a][b] < c: arr[a][b] = c

for i in range(1, N):
    for j in range(2, N):
        if arr[i][j - 1] and arr[i][j] < arr[i][j - 1] - 1: arr[i][j] = arr[i][j - 1] - 1

for j in range(1, N):
    if arr[0][j]: ans += 1

for i in range(1, N):
    for j in range(2, N):
        if arr[j - 1][i] and arr[j][i] < arr[j - 1][i] - 1:
            arr[j][i] = arr[j - 1][i] - 1
            ans += 1
        elif arr[j][i]: ans += 1

print(ans)


# 이중 for문 한 번만 돌기
import sys
input = sys.stdin.readline

N = 2002
arr = [[0] * N for _ in range(N)]
ans = 0

for i in range(int(input())):
    a, b, c = map(int, input().split())
    if arr[a][b] < c: arr[a][b] = c

for i in range(1, N - 1):
    for j in range(1, N - 1):
        if arr[i][j]:
            ans += 1
            x = arr[i][j]
            if arr[i + 1][j] <= x - 1: arr[i + 1][j] = x - 1
            if arr[i][j + 1] <= x - 1: arr[i][j + 1] = x - 1

print(ans)
