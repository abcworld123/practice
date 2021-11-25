import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append((e, -1))
    arr.append((s, 1))
arr.sort()

ans, cur = 0, 0
for x in arr:
    cur += x[1]
    if ans < cur: ans = cur

print(ans)
