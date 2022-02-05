import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [[0] * (C + 2)] + [[0] + list(map(int, input().rstrip())) + [0] for _ in range(R)] + [[0] * (C + 2)]
dp = [[[0, 0] for j in range(C + 2)] for i in range(R + 2)]
max_size = min(R, C) + 1 >> 1
atlst = False

for i in range(1, R + 1):
    for j in range(1, C + 1):
        if arr[i][j]:
            atlst = True
            dp[i][j][0] = dp[i - 1][j + 1][0] + 1
            dp[i][j][1] = dp[i - 1][j - 1][1] + 1

if not atlst: print(0); exit()
ans = 1

for i in range(2, R):
    if R - i < ans or ans == max_size: break
    for j in range(1, C):
        for k in range(dp[i][j][0] - 1, ans - 1, -1):
            if j + 2 * k <= C and i + k <= R and dp[i][j + 2 * k][1] > k and dp[i + k][j + k][0] > k and dp[i + k][j + k][1] > k:
                ans = k + 1
                break

print(ans)

# n^3 + 휴리스틱
# '/' 대각선만 빼곡히 있는 입력 주어지면 터짐..
