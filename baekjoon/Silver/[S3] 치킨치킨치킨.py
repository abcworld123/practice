from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for a, b, c in combinations(range(M), 3):
    ans = max(ans, sum(max((x[a], x[b], x[c])) for x in arr))

print(ans)
