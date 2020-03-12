import sys, heapq

V, E = map(int, input().split())
start = int(input())
graph, path = {}, [0]

for i in range(1, V + 1): graph[i] = []; path.append(999999)
for i in range(E):
	a, b, c = map(int, sys.stdin.readline().split())
	graph[a].append([b, c])
path[start] = 0
heap = [(0, start)]

while heap:
	cur = heapq.heappop(heap)[1]
	for v in graph[cur]:
		if path[cur] + v[1] < path[v[0]]: path[v[0]] = path[cur] + v[1]; heapq.heappush(heap, (path[v[0]], v[0]))

for p in path[1:]:
	print(p if p != 999999 else "INF")
