import heapq
import sys
input = sys.stdin.readline


def solution(op):
	maxheap, minheap = [], []
	visited = [False] * 1000000
	cnt = 0
	for i in range(len(op)):
		if op[i][0] == 'I':
			n = int(op[i][2:])
			heapq.heappush(maxheap, (-n, i))
			heapq.heappush(minheap, (n, i))
			cnt += 1
		elif cnt == 0: continue
		elif len(op[i]) == 4:
			while maxheap:
				x = heapq.heappop(maxheap)[1]
				if not visited[x]:
					visited[x] = True
					cnt -= 1
					break
		else:
			while minheap:
				x = heapq.heappop(minheap)[1]
				if not visited[x]:
					visited[x] = True
					cnt -= 1
					break
	if cnt == 0: print('EMPTY')
	else:
		max_n, min_n = 0, 0
		while maxheap:
			n, i = heapq.heappop(maxheap)
			if not visited[i]:
				max_n = -n
				break
		while minheap:
			n, i = heapq.heappop(minheap)
			if not visited[i]:
				min_n = n
				break
		return print(max_n, min_n)


for case in range(int(input())):
	arr = [input() for _ in range(int(input()))]
	solution(arr)
