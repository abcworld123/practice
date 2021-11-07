N, S = map(int, input().split())
arr = [0] + [*map(int, input().split())]
for i in range(1, len(arr)): arr[i] += arr[i - 1]
a, b = 0, 1
ans = 999999

while a < b < len(arr):
	if arr[b] - arr[a] >= S:
		if b - a < ans: ans = b - a
		a += 1
	else:
		b += 1

print(ans if ans != 999999 else 0)
