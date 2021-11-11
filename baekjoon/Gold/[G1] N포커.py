import math

n = int(input())
cards = 52 + 1
ncr = [[0] * cards for _ in range(cards)]

for i in range(cards):
    for j in range(cards):
        ncr[i][j] = math.comb(i, j)

mul = [[0] * 37 for _ in range(13)]
mul[0][0] = 1

for i in range(1, 13):
    for j in range(1 + 3 * i):
        mul[i][j] = sum(mul[i - 1][max(0, j - 3): min(j, 33) + 1])

ans = 0
for i in range(48, 35, -1):
    for j in range(n - 4, max(-1, n - (3 * (48 - i) + 5)), -1):
        if i < j: break
        ans += ncr[i - (n - 4 - j)][j] * mul[48 - i][n - 4 - j]

print(ans % 10007)

# 너무 어렵게 푼 듯...
