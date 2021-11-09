import sys
input = sys.stdin.readline

N = int(input())
fibo, fibo2 = [0, 1], [0] * N
for i in range(2, N + 1): fibo.append((fibo[-2] + fibo[-1]) % 1000000007)

for i in range(int(input())):
    l, r = map(int, input().split())
    fibo2[l - 1] += 1
    if r + 1 <= N: fibo2[r] -= fibo[r - l + 2]
    if r + 2 <= N: fibo2[r + 1] -= fibo[r - l + 1]

if N == 1: print(fibo2[0])
else:
    fibo2[1] += fibo2[0]
    for i in range(2, N): fibo2[i] = (fibo2[i - 2] + fibo2[i - 1] + fibo2[i]) % 1000000007
    print(*fibo2)
