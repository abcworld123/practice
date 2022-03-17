import sys
stdin = sys.stdin.buffer

N, H = map(int, stdin.readline().split())
arr = list(map(int, stdin.read().split()))
imos = [0] * H
imos[0] = N >> 1
a, b = imos[0], 1

for i in range(0, N, 2): imos[arr[i]] -= 1
for i in range(1, N, 2): imos[-arr[i]] += 1
for i in range(1, H):
    imos[i] += imos[i - 1]
    if imos[i] <= a:
        if imos[i] == a: b += 1
        else: a,b = imos[i], 1

print(a, b)
