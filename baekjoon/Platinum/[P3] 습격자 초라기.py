import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
inf = 99999

def make(arr1, arr2, dp, n):
    for i in range(1, n):
        cur = [inf] * 5
        if arr1[i - 1] + arr1[i] <= W:
            if arr2[i - 1] + arr2[i] <= W: cur[0] = dp[-1][3]
            cur[2] = (dp[-1][1] if dp[-1][1] < dp[-1][3] else dp[-1][3]) + 1
        if arr2[i - 1] + arr2[i] <= W: cur[1] = (dp[-1][2] if dp[-1][2] < dp[-1][3] else dp[-1][3]) + 1
        cur[3] = min(dp[-1]) + 2
        if arr1[i] + arr2[i] <= W: cur[4] = cur[3] - 1
        dp.append(cur)


for T in range(int(input())):
    N, W = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    c1, c2, c3 = arr1[0] + arr1[-1] <= W, arr2[0] + arr2[-1] <= W, arr1[0] + arr2[0] <= W
    if N == 1: print(1 if c3 else 2); continue
    ans = []

    if c1 and c2:
        dp = [[2, inf, inf, inf, inf]]
        make(arr1, arr2, dp, N - 1)
        ans.append(min(dp[-1]))
    if c2:
        dp = [[inf, 2, inf, inf, inf]]
        make(arr1, arr2, dp, N - 1)
        ans.append(min(min(dp[-1]) + 1, min(dp[-1][1], dp[-1][3]) if arr1[-2] + arr1[-1] <= W else inf))
    if c1:
        dp = [[inf, inf, 2, inf, inf]]
        make(arr1, arr2, dp, N - 1)
        ans.append(min(min(dp[-1]) + 1, min(dp[-1][2], dp[-1][3]) if arr2[-2] + arr2[-1] <= W else inf))
    if True:
        dp = [[inf, inf, inf, 2, 1 if c3 else inf]]
        make(arr1, arr2, dp, N)
        ans.append(min(dp[-1]))

    print(min(ans))
