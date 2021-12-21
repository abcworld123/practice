from decimal import *

def sin(x):
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


getcontext().rounding = ROUND_HALF_UP
pi = Decimal("3.141592653589793238462643383279")

A, B, C = map(Decimal, input().split())
s = (C - B) / A
e = (C + B) / A

if pi <= (s - pi / 2 + 50000 * pi) % (2 * pi):
    l = ((s - pi / 2) // (2 * pi) * 4 + 3) / 2
    if s - pi / 2 < 0: l -= 2
elif pi <= (e - pi / 2 + 50000 * pi) % (2 * pi):
    l = ((e - pi / 2) // (2 * pi) * 4 + 3) / 2
    if e - pi / 2 < 0: l -= 2
else:
    l = ((s - pi / 2) // (2 * pi) * 4 + 1) / 2
    if s - pi / 2 < 0: l -= 2
r = l + 1

m = 0
for _ in range(40):
    m = (l + r) / 2
    if -B * sin(m * pi % (2 * pi)) < A * m * pi - C: r = m
    else: l = m

print(m * pi)


# 생각해보니 24~33 라인이 필요 없었다...
