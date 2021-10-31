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
N, M = map(int, stdin[0].split())
arr = [0] * (N + 1)
fwtree = arr[:]
init(fwtree, N, arr)

for i in range(1, M + 1):
	op, a, b = map(int, stdin[i].split())
	if op == 1: update(fwtree, arr, N, a, b - arr[a])
	else:
		if a > b: a, b = b, a
		print(summ(fwtree, b) - summ(fwtree, a - 1))
