from fractions import Fraction

L = []
types = {'-': 0, '|': 1, '/': 2}
for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 > x2) or (x1 == x2 and y1 > y2): x1, y1, x2, y2 = x2, y2, x1, y1
    _type = '|' if x1 == x2 else '-' if y1 == y2 else '/'
    L.append((_type, x1, y1, x2, y2))

L.sort(key=lambda l: (types[l[0]], l[1], l[2]))
x1, y1, x2, y2 = L[0][1:]
x3, y3, x4, y4 = L[1][1:]
check = L[0][0] + L[1][0]

def p(*args):
    print(args[0])
    if len(args) > 1: print(*map(float, args[1:]))
    exit()

if check == '--':
    if y1 == y3 and x3 <= x2:
        if x3 == x2: p(1, x3, y3)
        else: p(1)

elif check == '||':
    if x1 == x3 and y3 <= y2:
        if y3 == y2: p(1, x3, y3)
        else: p(1)

elif check == '-|':
    if x1 <= x3 <= x2 and y3 <= y1 <= y4: p(1, x3, y1)

else:  # 'x/'
    c = Fraction(y4 - y3, x4 - x3)
    d = y3 - x3 * c

    if check == '-/':
        x = Fraction(y1 - d, c)
        if min(y3, y4) <= y1 <= max(y3, y4) and x1 <= x <= x2: p(1, x, y1)

    elif check == '|/':
        y = c * x1 + d
        if x3 <= x1 <= x4 and y1 <= y <= y2: p(1, x1, y)

    else:  # '//', '/\'
        a = Fraction(y2 - y1, x2 - x1)
        b = y1 - x1 * a
        if a == c:
            if b == d:
                if x3 <= x2:
                    if x3 == x2: p(1, x2, a * x2 + b)
                    else: p(1)
        else:
            x = Fraction(d - b, a - c)
            if x1 <= x <= x2 and x3 <= x <= x4: p(1, x, a * x + b)

p(0)
