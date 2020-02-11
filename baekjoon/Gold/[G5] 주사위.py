n = int(input())
a, b, c, d, e, f = map(int, input().split())

if n == 1: print(a+b+c+d+e+f - max(a, b, c, d, e, f))
else:
    one = min(a, b, c, d, e, f) * ((n-2)**2 + (n-1)*(n-2)*4)
    two = min(a+b, a+c, a+d, a+e, b+c, b+d, b+f, c+e, c+f, d+e, d+f, e+f) * (2 * n-3) * 4
    thr = min(a+b+c, a+b+d, a+c+e, a+d+e, b+c+f, b+d+f, c+e+f, d+e+f) * 4
    print(one + two + thr)
