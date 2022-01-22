from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
s = set(range(N))
ans = float('inf')
for c1 in combinations(range(N), N >> 1):
    if c1[0] == 1: break
    c2 = s - set(c1)
    s1, s2 = 0, 0
    for x1 in c1:
        for x2 in c1:
            if x1 == x2: continue
            else: s1 += arr[x1][x2]
    for x1 in c2:
        for x2 in c2:
            if x1 == x2: continue
            else: s2 += arr[x1][x2]
    ans = min(ans, abs(s1 - s2))

print(ans)
