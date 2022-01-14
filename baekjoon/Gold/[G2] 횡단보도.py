import os, io
from heapq import heappush, heappop
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inf = float('inf')
djk = [0, 0] + [inf] * (N - 1)
heap = [(0, 1)]

for i in range(1, M + 1):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

while heap[0][1] != N:
    cur = heappop(heap)[1]
    for v, c in graph[cur]:
        c = (c - djk[cur]) % M
        if c == 0: c = M
        if djk[cur] + c < djk[v]:
            djk[v] = djk[cur] + c
            heappush(heap, (djk[v], v))

print(djk[-1])
