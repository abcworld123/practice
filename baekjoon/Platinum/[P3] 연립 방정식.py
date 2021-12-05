from fractions import Fraction

T = int(input())
for case in range(T):
    e1l, e1r = map(str.split, input().split('='))
    e2l, e2r = map(str.split, input().split('='))

    d1l = {'y': 0, 'x': 0, 'c': 0}
    d1r, d2l, d2r = d1l.copy(), d1l.copy(), d1l.copy()
    arr = [(e1l, d1l), (e1r, d1r), (e2l, d2l), (e2r, d2r)]

    for e, d in arr:
        for i in range(0, len(e), 2):
            t = e[i][-1]
            sign = 1 if i == 0 or e[i - 1][0] == '+' else -1
            if t == 'x' or t == 'y': d[t] += (1 if len(e[i]) == 1 else -1 if e[i][-2] == '-' else int(e[i][:-1])) * sign
            else: d['c'] += int(e[i]) * sign

    d1x, d1y, d1c = d1r['x'] - d1l['x'], d1l['y'] - d1r['y'], d1r['c'] - d1l['c']
    d2x, d2y, d2c = d2r['x'] - d2l['x'], d2l['y'] - d2r['y'], d2r['c'] - d2l['c']

    s1 = Fraction(d1x, d1y) if d1y else 'inf' if d1x else '?'
    s2 = Fraction(d2x, d2y) if d2y else 'inf' if d2x else '?'
    y1 = Fraction(d1c, d1y) if d1y else -Fraction(d1c, d1x) if d1x else '?'
    y2 = Fraction(d2c, d2y) if d2y else -Fraction(d2c, d2x) if d2x else '?'
    if s2 == '?': s1, s2 = s2, s1; y1, y2 = y2, y1

    dk = "don't know"
    if d1x == 0 and d1y == 0 and d1c: x = y = dk
    elif d2x == 0 and d2y == 0 and d2c: x = y = dk
    elif s1 == s2:
        if s1 == 0 and y1 == y2: x = dk; y = y1
        elif s1 == 'inf' and y1 == y2: x = y1; y = dk
        else: x = y = dk
    elif s1 == '?':
        if s2 == 0: x = dk; y = y2
        elif s2 == 'inf': x = y2; y = dk
        else: x = y = dk
    elif s1 == 0 and s2 == 'inf': x = y2; y = y1
    elif s2 == 0 and s1 == 'inf': x = y1; y = y2
    elif s1 == 'inf': x = y1; y = s2 * x + y2
    elif s2 == 'inf': x = y2; y = s1 * x + y1
    else: x = Fraction(y2 - y1, s1 - s2); y = s1 * x + y1

    print(x)
    print(y)
    if case != T - 1:
        print()
        input()


# 문제가 참.. ㅎ
