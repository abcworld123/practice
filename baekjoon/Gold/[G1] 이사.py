import sys
input = sys.stdin.readline

N = int(input())
p = [tuple(map(int, input().split())) for _ in range(N)]
maxp = [0] * N

for i in range(len(p)):
	for j in range(i + 1, len(p)):
		d = (p[i][0] - p[j][0]) * (p[i][0] - p[j][0]) + (p[i][1] - p[j][1]) * (p[i][1] - p[j][1])
		if maxp[i] < d: maxp[i] = d
		if maxp[j] < d: maxp[j] = d

print(*p[maxp.index(min(maxp))])
