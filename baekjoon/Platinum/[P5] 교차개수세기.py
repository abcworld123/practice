import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
fw = [0] * (N + 1)
ans = 0

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

for x in arr:
    if not x: continue
    for v in sorted(x):
        i, j = N - v, N - v + 1
        while i: ans += fw[i]; i -= i & -i
        while j <= N: fw[j] += 1; j += j & -j

print(ans)
