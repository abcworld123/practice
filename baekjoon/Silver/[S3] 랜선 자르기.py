import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = tuple(map(int, sys.stdin))
l, r = 1, max(arr)
m = (l + r) >> 1
ans = 0

while l <= r:
    m = (l + r) >> 1
    total = sum((x // m for x in arr))
    if total >= N: ans = max(ans, m); l = m + 1
    else: r = m - 1

print(ans)
