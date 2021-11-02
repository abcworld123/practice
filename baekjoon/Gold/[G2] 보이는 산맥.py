import sys

length = 0
n = int(input())
arr = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: x[0])

start, end = arr[0][0], arr[0][1]
area = (end - start) ** 2

for i in range(1, n):
	if arr[i][0] < end:
		if arr[i][1] <= end: continue
		else: area -= (end - arr[i][0]) ** 2
	area += (arr[i][1] - arr[i][0]) ** 2
	end = arr[i][1]

print(area)
