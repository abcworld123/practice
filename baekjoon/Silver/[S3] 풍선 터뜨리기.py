N = int(input())
arr = list(map(int, input().split()))
for i in range(N): arr[i] = [i + 1, arr[i], True]

cur = 0
arr[0][2] = False
print(1, end=' ')

for i in range(N - 1):
	move = arr[cur][1]
	d = 1 if move > 0 else -1
	while move:
		cur += d
		if not 0 <= cur < N: cur %= N
		if arr[cur][2]: move -= d
	print(arr[cur][0], end=' ')
	arr[cur][2] = False
