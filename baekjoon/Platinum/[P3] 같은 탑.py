input()
dp = [0] * 500001
rb = 1

for x in map(int, input().split()):
	rb += x
	nxt = [0] * rb
	for i in range(min(rb, 250001)):
		if dp[i]:
			neg = abs(i - x)
			nxt[i + x] = max(nxt[i + x], dp[i] + x)
			nxt[neg] = max(dp[i], nxt[neg], dp[i] - i + x)
	for i in range(min(rb, 250001)):
		dp[i] = max(dp[i], nxt[i])
	dp[x] = max(dp[x], x)

print(dp[0] or -1)



# 테스트용 코드
from itertools import combinations

arr = [5,2,3,6,4,8,10,13,15,36, 20, 31 , 41, 50]

srr = set(arr)
ans = [0, None, None]

for i in range(1, len(arr) + 1):
	for c1 in combinations(arr, i):
		s1 = sum(c1)
		diff = srr - set(c1)
		for j in range(1, len(diff) + 1):
			for c2 in combinations(diff, j):
				s2 = sum(c2)
				if s1 == s2 and ans[0] < s1:
					ans = [s1, c1, c2]
					print(*ans)

# print(*ans)
