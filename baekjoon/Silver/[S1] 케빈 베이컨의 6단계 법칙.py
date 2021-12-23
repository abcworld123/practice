import sys
input = sys.stdin.readline

def bfs(graph, visited, q):
    for v, c in q:
        for b in graph[v]:
            if visited[b] == -1:
                visited[b] = c + 1
                q.append((b, c + 1))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
ans = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    visited = [-1] * (N + 1)
    visited[i] = 0
    bfs(graph, visited, [(i, 0)])
    ans.append(sum(visited) + 1)

_min = min(ans)
print(min(a for a, s in enumerate(ans, start=1) if s == _min))
