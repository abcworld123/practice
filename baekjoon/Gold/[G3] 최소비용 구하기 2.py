import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph, path, dup = {}, [0], {}

for i in range(1, n + 1):
	graph[i] = []
	path.append([float('inf'), 0])

for i in range(m):
	a, b, c = map(int, input().split())
	if (a, b) in dup:
		if dup[(a, b)] > c: dup[(a, b)] = min(dup[(a, b)], c)
	else:
		dup[(a, b)] = c

for x in dup.keys(): graph[x[0]].append((x[1], dup[x]))

start, end = map(int, input().split())
path[start][0] = 0
heap = [(0, start)]

while heap:
	cur = heapq.heappop(heap)[1]
	for v in graph[cur]:
		if path[cur][0] + v[1] < path[v[0]][0]:
			path[v[0]][0] = path[cur][0] + v[1]
			path[v[0]][1] = cur
			heapq.heappush(heap, (path[v[0]], v[0]))



ans, _from = [end], path[end][1]
while _from:
	ans.append(_from)
	_from = path[_from][1]

print(path[end][0])
print(len(ans))
print(*ans[::-1])
