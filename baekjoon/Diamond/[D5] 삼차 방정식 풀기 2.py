from decimal import *
getcontext().prec = 50

def f(x):
    return a*x*x*x + b*x*x + c*x + d

def bisect(l, r, flag):
    m = 0
    for _ in range(60):
        m = (l + r) / 2
        if f(m) * flag < 0: l = m
        else: r = m
    return format(round(m, 15), 'f')

lb, rb, small = Decimal('-1E6'), Decimal('1E6'), Decimal('1E-15')

for _ in range(int(input())):
    a, b, c, d = map(Decimal, input().rstrip().split())
    if a < 0: a, b, c, d = -a, -b, -c, -d
    a2, b2 = 3*a, 2*b
    D2 = b2*b2 - 4*a2*c
    D3 = b*b*c*c - 4*b*b*b*d - 4*c*c*c*a + 18*a*b*c*d - 27*a*a*d*d
    if D2 <= 0:
        print(bisect(lb, rb, 1))
    else:
        x1 = (-b2 - D2.sqrt()) / (2 * a2)
        x2 = (-b2 + D2.sqrt()) / (2 * a2)
        if D3 > 0:
            print(bisect(lb, x1, 1), bisect(x1, x2, -1), bisect(x2, rb, 1))
        elif D3 < 0:
            if f(x1) < 0:
                print(bisect(x2, rb, 1))
            else:
                print(bisect(lb, x1, 1))
        else:
            if abs(f(x1)) < small:
                print(x1, bisect(x2, rb, 1))
            else:
                print(bisect(lb, x1, 1), x2)


# 맞왜틀 코드 (중근 판별에서 잘못된 것 같음)
from decimal import *
getcontext().prec = 100

def f(x):
    return a*x*x*x + b*x*x + c*x + d

def bisect(l, r, flag):
    m = 0
    for _ in range(100):
        m = (l + r) / 2
        if f(m) * flag < 0: l = m
        else: r = m
    return format(round(m, 15), 'f')

lb, rb, small = Decimal('-1E6'), Decimal('1E6'), Decimal('1E-15')

for _ in range(int(input())):
    a, b, c, d = map(Decimal, input().rstrip().split())
    if a < 0: a, b, c, d = -a, -b, -c, -d
    a2, b2 = 3 * a, 2 * b
    D2 = b2 * b2 - 4 * a2 * c
    if D2 <= 0: print(bisect(lb, rb, 1))
    else:
        x1 = (-b2 - D2.sqrt()) / (2 * a2)
        x2 = (-b2 + D2.sqrt()) / (2 * a2)
        if f(x1) < 0: print(bisect(x2, rb, 1))
        elif f(x2) > 0: print(bisect(lb, x1, 1))
        elif abs(f(x1)) < small: print(x1, bisect(x2, rb, 1))
        elif abs(f(x2)) < small: print(bisect(lb, x1, 1), x2)
        else: print(bisect(lb, x1, 1), bisect(x1, x2, -1), bisect(x2, rb, 1))
