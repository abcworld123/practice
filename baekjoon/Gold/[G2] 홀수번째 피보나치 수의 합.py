def f(fibo, n, m):
    if n < 3: return fibo[n] % m
    half, odd = n >> 1, n & 1
    if half not in fibo: fibo[half] = f(fibo, half, m)
    if half + 1 not in fibo: fibo[half + 1] = f(fibo, half + 1, m)
    if not odd and half - 1 not in fibo: fibo[half - 1] = f(fibo, half - 1, m)
    return (fibo[half + odd] * fibo[half + 1] + fibo[half - 1 + odd] * fibo[half]) % m

n = int(input())
fibo = {0: 0, 1: 1, 2: 1}
print(f(fibo, n + (n & 1), 1000000007))
