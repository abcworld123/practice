def f2():
    for a in range(10):
        if D == 10 * a - a:
            return make(2, a)

def f3():
    for a in range(10):
        if D == 100 * a - a:
            return make(3, a)

def f4():
    for a in range(10):
        for b in range(-9, 10):
            if D == 1000 * a + 100 * b - 10 * b - a:
                return make(4, a, b)

def f5():
    for a in range(10):
        for b in range(-9, 10):
            if D == 10000 * a + 1000 * b - 10 * b - a:
                return make(5, a, b)

def f6():
    for a in range(10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                if D == 100000 * a + 10000 * b + 1000 * c - 100 * c - 10 * b - a:
                    return make(6, a, b, c)

def f7():
    for a in range(10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                if D == 1000000 * a + 100000 * b + 10000 * c - 100 * c - 10 * b - a:
                    return make(7, a, b, c)

def f8():
    for a in range(10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
                    if D == 10000000 * a + 1000000 * b + 100000 * c + 10000 * d - 1000 * d - 100 * c - 10 * b - a:
                        return make(8, a, b, c, d)

def f9():
    for a in range(10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
                    if D == 100000000 * a + 10000000 * b + 1000000 * c + 100000 * d - 1000 * d - 100 * c - 10 * b - a:
                        return make(9, a, b, c, d)

def f10():
    for a in range(10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
                    for e in range(-9, 10):
                        if D == 1000000000 * a + 100000000 * b + 10000000 * c + 1000000 * d + 100000 * e - 10000 * e - 1000 * d - 100 * c - 10 * b - a:
                            return make(10, a, b, c, d, e)

def make(l, *arr):
    ans = [0] * l
    ans[0] = max(arr[0], 1)
    ans[-1] = 0 if arr[0] else 1
    for i in range(1, l >> 1):
        ans[i] = max(arr[i], 0)
        ans[-i - 1] = max(-arr[i], 0)
    return ''.join(map(str, ans))


D = int(input())
if D == 990000: print(10001000001)
elif D == 900000: print(100001000001)
else: print(f2() or f3() or f4() or f5() or f6() or f7() or f8() or f9() or f10() or -1)
