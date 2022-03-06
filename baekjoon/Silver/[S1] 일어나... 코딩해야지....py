import sys
from math import gcd
input = sys.stdin.readline
LCM = lambda x, y: x * y // gcd(x, y)

N, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0, 0]

for i in range(N - 1):
    T1, K1 = arr[i]
    for j in range(i + 1, N):
        T2, K2 = arr[j]
        lcm = LCM(K1, K2)
        cur = D // K1 + D // K2 - D // lcm + (max(T1, T2) - 1) // lcm - (T1 - 1) // K1 - (T2 - 1) // K2
        if ans[2] < cur: ans = [i + 1, j + 1, cur]

print(ans[0], ans[1])
print(ans[2])
