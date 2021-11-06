N = int(input())
arr = tuple(tuple(map(int, input().split())) for _ in range(N))
ans = 0
blue, white = 0, 0

def f(x1, y1, x3, y3):
	global ans, blue, white
	if x3 - x1 == 1:
		if arr[y1][x1]: blue += 1
		else: white += 1
		return arr[y1][x1], True
	x2, y2 = (x1 + x3) >> 1, (y1 + y3) >> 1
	a1, b1 = f(x1, y1, x2, y2)
	a2, b2 = f(x2, y1, x3, y2)
	a3, b3 = f(x1, y2, x2, y3)
	a4, b4 = f(x2, y2, x3, y3)
	if a1 == a2 == a3 == a4 and b1 and b2 and b3 and b4:
		if a1: blue -= 3
		else: white -= 3
		return arr[y1][x1], True
	else: return 0, False

f(0, 0, N, N)
print(white)
print(blue)
