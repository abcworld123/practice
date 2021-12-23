from math import gcd

for T in range(int(input())):
    M, N, x, y = map(int, input().split())
    if x == M: x = 0
    for i in range(M * N // gcd(M, N) // N):
        if (N * i + y) % M == x:
            print(N * i + y)
            break
    else: print(-1)
