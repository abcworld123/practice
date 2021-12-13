
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
graph = [[] for _ in range(N)]
R = [-1] * N
ans = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)

for i in range(N):
    if dfs([False] * N, i): ans += 1

print(ans)
