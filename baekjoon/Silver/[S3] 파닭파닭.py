import sys

S, C = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin))
l, r = 1, max(arr)
m = (l + r) >> 1
ans = 0

while l <= r:
    m = (l + r) >> 1
    total = sum((x // m for x in arr))
    if total >= C: ans = max(ans, m); l = m + 1
    else: r = m - 1

print(sum(arr) - ans * C)
