import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N)]
ans = [set() for _ in range(N)]

for a in range(N):
    for b, v in enumerate(map(int, input().split())):
        if v: graph[a].append(b)

for a in range(N):
    q = [a]
    visited = [False] * N
    for v in q:
        for b in graph[v]:
            if visited[b]: continue
            visited[b] = True
            if a == b: ans[a].add(a)
            elif not ans[b]:
                q.append(b)
                ans[a].add(b)
            else:
                ans[a] |= ans[b]
                ans[a].add(b)

for a in ans:
    line = [0] * N
    for v in a: line[v] = 1
    print(' '.join(map(str, line)))
