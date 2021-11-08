import sys
input = sys.stdin.readline


def init(odd, even, N, arr):
	for i in range(1, N + 1):
		for j in range(i - (i & -i), i):
			if arr[j + 1] & 1: odd[i] += 1
			else: even[i] += 1


def get(fwtree, i):
	total = 0
	while i:
		total += fwtree[i]
		i -= i & -i
	return total


def update(fwtree, N, i, diff):
	while i <= N:
		fwtree[i] += diff
		i += i & -i


N = int(input())
arr = [0] + list(map(int, input().split()))
odd, even = [0] * (N + 1), [0] * (N + 1)
init(odd, even, N, arr)

for i in range(int(input())):
	op, a, b = map(int, input().split())
	if op == 1 and (b - arr[a]) & 1:
		if b & 1:
			update(odd, N, a, 1)
			update(even, N, a, -1)
		else:
			update(odd, N, a, -1)
			update(even, N, a, 1)
		arr[a] = b
	elif op == 2: print(get(even, b) - get(even, a - 1))
	elif op == 3: print(get(odd, b) - get(odd, a - 1))
