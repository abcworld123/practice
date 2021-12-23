import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
visited = [False] * (N + 1)
ans = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for a in range(1, N + 1):
    if not visited[a]:
        ans += 1
        visited[a] = True
        q = [a]
        for v in q:
            for b in graph[v]:
                if not visited[b]:
                    visited[b] = True
                    q.append(b)

print(ans)
