import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
ans = [0, 0, 10 ** 9]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for c1, c2 in combinations(range(1, N + 1), 2):
    dist = [-1] * (N + 1)
    cnt = N - 2
    dist[c1] = 0
    dist[c2] = 0
    q = [(c1, 0), (c2, 0)]
    for u, d in q:
        for v in graph[u]:
            if dist[v] == -1:
                cnt -= 1
                dist[v] = d + 1
                if cnt == 0: break
                q.append((v, d + 1))
        else: continue
        break
    cur = (sum(dist) + 1) * 2
    if cur < ans[2]:
        ans = [c1, c2, cur]

print(*ans)
