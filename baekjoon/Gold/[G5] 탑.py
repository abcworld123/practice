N = int(input())
tower = [*map(int, input().split())]
stack, ans = [], []

for i in range(len(tower)):
	while stack and stack[-1][0] < tower[i]: stack.pop()
	if not stack: ans.append(0)
	else: ans.append(stack[-1][1])
	stack.append((tower[i], i + 1))

print(*ans)
