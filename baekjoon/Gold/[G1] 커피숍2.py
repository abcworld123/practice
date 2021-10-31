def init(fwtree, N, arr):
	for i in range(1, N + 1):
		for j in range(i - (i & -i), i):
			fwtree[i] += arr[j + 1]
	return fwtree


def summ(fwtree, i):
	total = 0
	while i:
		total += fwtree[i]
		i -= i & -i
	return total


def update(fwtree, arr, N, i, diff):
	arr[i] += diff
	while i <= N:
		fwtree[i] += diff
		i += i & -i


stdin = [*open(0)]
N, Q = map(int, stdin[0].split())
arr = [0] + list(map(int, stdin[1].split()))
fwtree = [0] * (N + 1)
init(fwtree, N, arr)

for i in range(2, Q + 2):
	x, y, a, b = map(int, stdin[i].split())
	if x > y: x, y = y, x
	print(summ(fwtree, y) - summ(fwtree, x - 1))
	update(fwtree, arr, N, a, b - arr[a])
