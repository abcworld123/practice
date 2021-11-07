import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
stack, ans = [], 0

for x in arr:
	while stack and stack[-1] <= x: stack.pop()
	ans += len(stack)
	stack.append(x)

print(ans)
