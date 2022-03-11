import os, io, sys
sys.setrecursionlimit(123500)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def dfs(v):
    visited[v] = 1
    for u in graph[v]:
        if not visited[u]:
            nums[v] += dfs(u)
    return max(nums[v], 0)


N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
nums = [0] * (N + 1)
visited[1] = 1

for v in range(2, N + 1):
    t, n, u = input().split()
    n, u = int(n), int(u)
    graph[u].append(v)
    graph[v].append(u)
    nums[v] = n if t == b'S' else -n

dfs(1)
print(nums[1])
