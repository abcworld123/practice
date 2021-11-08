n = int(input())
arr = [[[0] * 1024 for _ in range(10)] for _ in range(n + 1)]
for j in range(1, 10): arr[1][j][1 << j] = 1

for i in range(1, n + 1):
	for j in range(10):
		for k in range(1024):
			if not k & 1 << j: continue
			if j > 0:
				arr[i][j][k] += arr[i - 1][j - 1][k & ~(1 << j)]
				arr[i][j][k] += arr[i - 1][j - 1][k]
			if j < 9:
				arr[i][j][k] += arr[i - 1][j + 1][k & ~(1 << j)]
				arr[i][j][k] += arr[i - 1][j + 1][k]

print(sum(arr[-1][j][1023] for j in range(10)) % 1000000000)

# 골드 중에 제일 헬이었음...
