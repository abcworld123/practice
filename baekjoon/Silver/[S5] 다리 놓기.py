for _ in range(int(input())):
    ans = 1
    r, n = map(int, input().split())
    for i in range(n, n - r, -1): ans *= i
    for i in range(r, 0, -1): ans //= i
    print(ans)
