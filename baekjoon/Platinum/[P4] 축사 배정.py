def dfs(visited, i):
    visited[i] = True
    for v in graph[i]:
        if R[v] == -1 or (not visited[R[v]] and dfs(visited, R[v])):
            L[i] = v; R[v] = i
            return True
    return False


N, M = map(int, input().split())
graph = []
L = [-1] * N
R = [-1] * M
ans = 0

for i in range(N):
    _, *want = map(int, input().split())
    graph.append([v - 1 for v in want])

for i in range(N):
    if L[i] == -1 and dfs([False] * N, i): ans += 1

print(ans)
