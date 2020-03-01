def DFS(v):
	visited_dfs[v] = 1
	print(v, end=' ')
	for x in graph[v]:
		if not visited_dfs[x]: DFS(x)


def BFS(v):
	visited_bfs[v] = 1
	queue = [v]
	print(v, end=' ')
	for x in queue:
		for y in graph[x]:
			if not visited_bfs[y]:
				visited_bfs[y] = 1
				queue.append(y)
				print(y, end=' ')


N, M, V = map(int, input().split())
graph, visited_dfs, visited_bfs = {}, {}, {}
for i in range(1, N + 1):
	graph[i] = []
	visited_dfs[i] = 0
	visited_bfs[i] = 0
for i in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
for v in graph: graph[v] = sorted(graph[v])
DFS(V)
print()
BFS(V)
