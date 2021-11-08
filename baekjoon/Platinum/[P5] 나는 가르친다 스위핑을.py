import sys
input = sys.stdin.readline

n = int(input())
lines = []
ans, count = 0, 0

for i in range(n):
	x1, y1, x2, y2 = map(int, input().split())
	s1, s2 = y1 / x1, y2 / x2
	if s1 > s2: s1, s2 = s2, s1
	lines.append((s1, 1))
	lines.append((s2, -1))
lines.sort(key=lambda x: (x[0], -x[1]))

for line in lines:
	count += line[1]
	if ans < count: ans = count

print(ans)
