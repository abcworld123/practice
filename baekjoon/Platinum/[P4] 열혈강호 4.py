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


N, M, K = map(int, input().split())
graph = []
L = [0] * N
R = [-1] * M
ans, _K = 0, K
remain = set()

for i in range(N):
    _, *want = list(map(int, input().split()))
    graph.append([v - 1 for v in want])
    if graph[i]: remain.add(i)

while 1:
    prev = ans
    full = set()
    for i in remain:
        if dfs([False] * N, i):
            ans += 1
            L[i] += 1
            if L[i] >= 2: _K -= 1
            if L[i] == len(graph[i]): full.add(i)
        if ans == M or ans == N + K or _K == 0: print(ans); exit()
    if prev == ans: break
    remain -= full

print(ans)
