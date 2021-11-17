from fractions import Fraction


def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def crosscheck(l1, l2):
    def check(a1, a2, b1, b2):
        if ccw(a1, a2, b1) * ccw(a1, a2, b2) == 0:
            if ccw(b1, b2, a1) * ccw(b1, b2, a2) == 0:
                if a1 > a2: a1, a2 = a2, a1
                if b1 > b2: b1, b2 = b2, b1
                if a2 >= b1 and a1 <= b2:
                    return True
                else:
                    return False
        if ccw(a1, a2, b1) * ccw(a1, a2, b2) <= 0:
            if ccw(b1, b2, a1) * ccw(b1, b2, a2) <= 0: return True
        return False

    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2
    if check((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
        try:
            x = Fraction(((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)), ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)))
            y = Fraction(((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)), ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)))
            return x, y
        except:
            a1 = [x1, y1]
            a2 = [x2, y2]
            b1 = [x3, y3]
            b2 = [x4, y4]
            if a1 > a2: a1, a2 = a2, a1
            if b1 > b2: b1, b2 = b2, b1
            if a2 == b1: return a2[0], a2[1]
            elif a1 == b2: return a1[0], a1[1]
    else:
        return False


def inout(bolok, p):
    if ccw(bolok[0], bolok[1], p) <= 0 or ccw(bolok[0], bolok[-1], p) >= 0: return False
    else:
        for i in range(1, len(bolok)):
            if ccw(bolok[0], bolok[i], p) < 0:
                if ccw(bolok[i - 1], p, bolok[i]) < 0: return True
                else: return False
        return False


N, M = map(int, input().split())
bolok = [
    [tuple(map(int, input().split())) for _ in range(N)],
    [tuple(map(int, input().split())) for _ in range(M)]
]

ans, nxt = [], ()
in_point = False

for i in range(len(bolok[0])):
    if inout(bolok[1], bolok[0][i]):
        ans.append(bolok[0][i])
        nxt = (0, i + 1)
        in_point = True
        break
else:
    for i in range(len(bolok[1])):
        if inout(bolok[0], bolok[1][i]):
            ans.append(bolok[1][i])
            nxt = (1, i + 1)
            in_point = True
            break

if in_point:
    bolok[0] *= 2
    bolok[1] *= 2
    while len(ans) == 1 or ans[0] != ans[-1]:
        color = nxt[0]
        i = nxt[1]
        line = (*ans[-1], *bolok[color][i])
        cross = []
        color2 = color ^ 1
        for j in range(len(bolok[color2]) - 1):
            point = crosscheck(line, (*bolok[color2][j], *bolok[color2][j + 1]))
            if point and point != ans[-1]:
                ans.append(point)
                nxt = (color2, j + 1)
                break
        else:
            ans.append(bolok[color][i])
            nxt = (color, i + 1)
    ans.pop()

else:
    for i in range(len(bolok[0])):
        points = []
        for j in range(len(bolok[1])):
            point = crosscheck((*bolok[0][i], *bolok[0][(i + 1) % len(bolok[0])]), (*bolok[1][j], *bolok[1][(j + 1) % len(bolok[1])]))
            if point: points.append(point)
        points.sort(key=lambda p: (bolok[0][i][0] - p[0]) ** 2 + (bolok[0][i][1] - p[1]) ** 2)
        ans += points

area = 0
for i in range(1, len(ans) - 1):
    x1, x2, x3 = ans[0][0], ans[i][0], ans[i + 1][0]
    y1, y2, y3 = ans[0][1], ans[i][1], ans[i + 1][1]
    area += Fraction(abs((x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)), 2)

print(float(area))

# 구현 난이도 hell
