N, L = map(int, input().split())
ans = []

for i in range(L, 101):
	if i % 2 == 0 and N % i == i // 2 and N // i - (i // 2) + 1 > -1: ans = [N // i - (i // 2) + 1 + x for x in range(i)]; break
	elif i % 2 and N % i == 0 and N // i - i // 2 > -1: ans = [N // i - i // 2 + x for x in range(i)]; break

if ans:
	for x in ans: print(x, end=' ')
else: print(-1)
