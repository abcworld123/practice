N = int(input())
dp = [False] * 40001

for x in map(int, input().split()):
    nxt = [False] * 15001
    for i in range(1, 14501):
        if dp[i]:
            nxt[i + x] = True
            nxt[abs(i - x)] = True
    for i in range(1, 15001):
        if nxt[i]: dp[i] = True
    dp[x] = True

input()
print(*['NY'[dp[x]] for x in map(int, input().split())])
