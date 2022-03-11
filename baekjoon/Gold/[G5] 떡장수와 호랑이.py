import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split()))[1:] for _ in range(N)]
dp = [[-1] * 10 for _ in range(N)]
for x in arr[0]: dp[0][x] = 0

for i in range(1, N):
    for x in arr[i]:
        for j in range(1, 10):
            if dp[i - 1][j] != -1 and x != j:
                dp[i][x] = j
                break

cur, ans = -1, []
for i in range(1, 10):
    if dp[-1][i] != -1:
        ans.append(i)
        cur = dp[-1][i]
        break
else:
    print(-1)
    exit()

for i in range(N - 2, -1, -1):
    ans.append(cur)
    cur = dp[i][cur]

print('\n'.join(map(str, ans[::-1])))
