import sys
import math
input = sys.stdin.readline


n = int(input())
balance = 0
m = 0
b_ = -1
flag = True
for i in range(n):
	a, b = map(int, input().split())
	m_ = b - a - balance
	if m_ < 0: flag = False
	elif m_ > 0:
		m = math.gcd(m_, m)
		b_ = max(b_, b)
	balance = b

if flag and m > b_: print(m or 1)
else: print(-1)


# 아직 약간 헷갈림
