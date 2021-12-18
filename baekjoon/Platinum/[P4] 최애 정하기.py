import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def dfs(visited, i):
    visited[i] = True
    for v in graph[i]:
        if R[v] == -1:
            R[v] = i
            return True
    for v in graph[i]:
        if not visited[R[v]] and dfs(visited, R[v]):
            R[v] = i
            return True
    return False


N, M = map(int, input().split())
graph = []
idol = {v: k for k, v in enumerate([input().rstrip() for _ in range(M)])}
R = [-1] * M
ans = 0

for i in range(N):
    _, *likes = input().split()
    graph.append([idol[x] for x in likes])

for i in range(N):
    if dfs([False] * N, i): ans += 1

print('YES' if ans == N else f'NO\n{ans}')
