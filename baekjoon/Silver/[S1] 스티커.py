import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for T in range(int(input())):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    dp1 = [0] * (N + 2)
    dp2 = [0] * (N + 2)
    for i in range(N):
        dp1[i + 1] = (dp2[i - 1] if dp2[i - 1] >= dp2[i] else dp2[i]) + arr1[i]
        dp2[i + 1] = (dp1[i - 1] if dp1[i - 1] >= dp1[i] else dp1[i]) + arr2[i]
    print(max(dp1[-2], dp2[-2]))
