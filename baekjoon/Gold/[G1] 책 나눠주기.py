import sys
input = sys.stdin.readline
sys.setrecursionlimit(1010)

def dfs(visited, pair, a):
    visited[a] = True
    for j in range(pair[a], len(graph[a])):
        b = graph[a][j]
        if R[b] == -1 or (not visited[R[b]] and dfs(visited, pair, R[b])):
            L[a] = b; R[b] = a; pair[a] = j
            return True
    return False


for T in range(int(input())):
    N, M = map(int, input().split())
    graph = []
    L = [-1] * M
    R = [-1] * N
    pair = [0] * M
    ans = 0

    for _ in range(M):
        a, b = map(int, input().split())
        graph.append(list(range(a - 1, b)))

    for a in range(M):
        if L[a] == -1 and dfs([False] * M, pair, a): ans += 1

    print(ans)
