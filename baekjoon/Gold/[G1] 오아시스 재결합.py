import sys
input = sys.stdin.readline

N = int(input())
stack = [[int(input()), 1]]
arr = [int(input()) for _ in range(N - 1)]
ans = 0

for x in arr:
	if stack[-1][0] > x:
		ans += 1
		stack.append([x, 1])
	else:
		while stack and stack[-1][0] < x:
			ans += stack[-1][1]
			stack.pop()
		if stack:
			if stack[-1][0] == x:
				if len(stack) >= 2: ans += 1
				ans += stack[-1][1]
				stack[-1][1] += 1
			else:
				ans += 1
				stack.append([x, 1])
		else:
			stack.append([x, 1])

print(ans)
