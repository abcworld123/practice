arr = []
s = set()

def rec(y, n):
    ans = 0
    for x in list(s):
        for i in range(1, y + 1):
            if abs(x - arr[y - i]) == i: break
        else:
            if y == n - 1:ans += 1
            else:
                arr[y] = x
                s.remove(x)
                ans += rec(y + 1, n)
                arr[y] = -1
                s.add(x)
    return ans

def solution(n):
    global arr, s
    s = {x for x in range(n)}
    arr = [-1] * n
    return rec(0, n)
