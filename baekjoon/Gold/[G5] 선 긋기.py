import sys

length = 0
n = int(input())
arr = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: x[0])

start, end = arr[0][0], arr[0][1]
for i in range(1, n):
	if end < arr[i][0]:
		length += end - start
		start = arr[i][0]
	if end < arr[i][1]: end = arr[i][1]
length += end - start

print(length)
