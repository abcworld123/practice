from heapq import heappush, heappop

N, D = map(int, input().split())
arr = list(map(int, input().split()))
cur = (float('inf'), -1)
heap, ans = [], []


for i in range(len(arr)):
	heappush(heap, (arr[i], i))
	while heap[0][1] < i - D + 1: heappop(heap)
	if cur[1] < i - D + 1 or heap[0][0] < cur[0]: cur = heappop(heap)
	ans.append(cur[0])

print(*ans)
