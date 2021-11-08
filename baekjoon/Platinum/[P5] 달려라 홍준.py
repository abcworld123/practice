import heapq, sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = tuple(map(lambda x: -int(x), input().split()))
heap = [(arr[i], i) for i in range(2 * M - 2)]
heapq.heapify(heap)

ans = []
for pos in range(M - 1, N - M + 1):
	heapq.heappush(heap, (arr[pos + M - 1], pos + M - 1))
	while not (-M < heap[0][1] - pos < M): heapq.heappop(heap)
	ans.append(-heap[0][0])

print(*ans)
