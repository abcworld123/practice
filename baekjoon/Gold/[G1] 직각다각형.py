import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
hor, ver = [], []

for i in range(n):
    if arr[i - 1][0] == arr[i][0]:
        a, b = arr[i - 1][1], arr[i][1]
        if a > b: a, b = b, a
        ver.append((b, -1))
        ver.append((a, 1))
    else:
        a, b = arr[i - 1][0], arr[i][0]
        if a > b: a, b = b, a
        hor.append((b, -1))
        hor.append((a, 1))

hor.sort()
ver.sort()

ans, cur = 0, 0
for x, flag in hor:
    cur += flag
    if ans < cur: ans = cur
for x, flag in ver:
    cur += flag
    if ans < cur: ans = cur

print(ans)
