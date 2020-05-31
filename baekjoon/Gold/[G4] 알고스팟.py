import heapq

line = ""
M, N = map(int, input().split())
for i in range(N): line += input()
maze = list(map(int, list(line)))
path = [200] * (N * M)
visited = [0] * (N * M)
path[0] = 0
heap = [(0, 0)]

while heap:
	v = heapq.heappop(heap)[1]
	if visited[v]: continue
	visited[v] = 1
	U, R, D, L = v - M, v + 1, v + M, v - 1
	if U >= 0 and path[U] > path[v] + maze[U]: path[U] = path[v] + maze[U]; heapq.heappush(heap, (path[U], U))
	if R < N * M and R % M and path[R] > path[v] + maze[R]: path[R] = path[v] + maze[R]; heapq.heappush(heap, (path[R], R))
	if D < N * M and path[D] > path[v] + maze[D]: path[D] = path[v] + maze[D]; heapq.heappush(heap, (path[D], D))
	if L % M != M - 1 and path[L] > path[v] + maze[L]: path[L] = path[v] + maze[L]; heapq.heappush(heap, (path[L], L))

print(path[N * M - 1])
