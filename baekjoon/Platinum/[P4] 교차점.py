import sys
from fractions import Fraction
input = sys.stdin.readline

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

def cross(l1, l2):
    def check(a1, a2, b1, b2):
        if ccw(a1, a2, b1) * ccw(a1, a2, b2) == 0:
            if ccw(b1, b2, a1) * ccw(b1, b2, a2) == 0:
                if a1 > a2: a1, a2 = a2, a1
                if b1 > b2: b1, b2 = b2, b1
                if a2 >= b1 and a1 <= b2: return True
                else: return False
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
            a1, a2, b1, b2 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]
            if a1 > a2: a1, a2 = a2, a1
            if b1 > b2: b1, b2 = b2, b1
            if a2 == b1: return a2[0], a2[1]
            elif a1 == b2: return a1[0], a1[1]
            return 4
    else:
        return 0


for T in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    l = list(map(int, input().split()))
    points = {cross(l, (x1, y1, x2, y1)), cross(l, (x1, y2, x2, y2)), cross(l, (x1, y1, x1, y2)), cross(l, (x2, y1, x2, y2))}
    if 4 in points: print(4)
    else: print(len(points - {0}))
