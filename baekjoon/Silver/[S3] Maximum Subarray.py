for _ in range(int(input())):
    ps, ans = 0, -999
    input()
    for x in map(int, input().split()):
        ans = max(ans, ps := max(ps + x, x))
    print(ans)
