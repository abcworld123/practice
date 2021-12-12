import sys
input = sys.stdin.readline

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
R = [-1] * M
ans = 0

for i in range(N):
    _, *want = map(int, input().split())
    graph.append([v - 1 for v in want])

for i in range(N):
    if dfs([False] * N, i): ans += 1
    if ans == M: break

print(ans)
