import sys

input()
arr = [list(map(int, x.split())) for x in sys.stdin.readlines()]

for i in range(1, len(arr)):
	arr[i - 1] = [0] + arr[i - 1] + [0]
	for j in range(len(arr[i])):
		arr[i][j] += max(arr[i - 1][j], arr[i - 1][j + 1])

print(max(arr[-1]))
