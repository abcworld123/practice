import sys
input = sys.stdin.readline

for case in range(int(input())):
	n = int(input())
	p = [tuple(map(int, input().split())) for _ in range(n)]
	dic = {x: True for x in p}
	ans = 0
	for i in range(len(p) - 1):
		a, b = p[i][0], p[i][1]
		for j in range(i + 1, len(p)):
			c, d = p[j][0], p[j][1]
			ca, bd = c - a, b - d
			if ((c + bd, d + ca) in dic and (a + bd, b + ca) in dic) or ((c - bd, d - ca) in dic and (a - bd, b - ca) in dic):
				area = ca ** 2 + bd ** 2
				if ans < area: ans = area
	print(ans)
