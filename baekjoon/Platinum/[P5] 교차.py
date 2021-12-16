import sys
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

    if check((l1[0], l1[1]), (l1[2], l1[3]), (l2[0], l2[1]), (l2[2], l2[3])): return True
    else: return False


for T in range(int(input())):
    arr = list(map(int, input().split()))
    l = arr[:4]
    x1, y1, x2, y2 = arr[4:]
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    if x1 <= l[0] <= x2 and x1 <= l[2] <= x2 and y1 <= l[1] <= y2 and y1 <= l[3] <= y2: print('T')
    else:
        if any((cross(l, (x1, y1, x2, y1)), cross(l, (x1, y2, x2, y2)), cross(l, (x1, y1, x1, y2)), cross(l, (x2, y1, x2, y2)))): print('T')
        else: print('F')
