import sys
input = sys.stdin.readline


N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

answer, mid = -1, -1
left, right = min(times) * M // len(times), max(times) * (M + 1) // len(times)

while left <= right:
	mid = (left + right) // 2
	total = sum((mid // t for t in times))
	if total >= M:
		answer = min(answer, mid) if answer != -1 else mid
		right = mid - 1
	else:
		left = mid + 1

print(answer if answer != -1 else mid)
