import sys
input = sys.stdin.readline

def dfs(visited, i):
    visited[i] = True
    for v in graph[i]:
        if R[v] == -1:
            R[v] = i
            return True
    for v in graph[i]:
        if not visited[R[v]] and R[v] != i and dfs(visited, R[v]):
            R[v] = i
            return True
    return False


N = int(input())
sharks = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
R = [-1] * N
ans = N

for i in range(N):
    for j in range(N):
        if i != j and all(sharks[i][k] >= sharks[j][k] for k in range(3)):
            if i > j and all(sharks[i][k] == sharks[j][k] for k in range(3)): continue
            graph[i].append(j)

for i in range(N):
    if dfs([False] * N, i): ans -= 1
    if ans == 1: break
    if dfs([False] * N, i): ans -= 1
    if ans == 1: break

print(ans)
