import sys
input = sys.stdin.readline


def prime(n):
    if n < 2: return []
    n += 1
    save = [1] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if save[i // 2]: save[i * i // 2::i] = [0] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]

def summ(fwtree, i):
    total = 0
    while i:
        total += fwtree[i]
        i -= i & -i
    return total

def update(fwtree, N, i):
    while i <= N:
        fwtree[i] += 1
        i += i & -i

N = 100000
divisors = [0] * (N + 1)
for p in prime(N):
    for i in range(p, len(divisors), p):
        divisors[i] = p

queries = [(1, *map(int, input().split()), i) for i in range(int(input()))] + [(0, i, divisors[i]) for i in range(2, N + 1)]
queries.sort(key=lambda x: (x[1], x[0]))
fwtree = [0] * (N + 1)
ans = []

for t, x, y, *e in queries:
    if t == 0: update(fwtree, N, y)
    else: ans.append((e[0], summ(fwtree, y)))

for a in sorted(ans, key=lambda x: x[0]): print(a[1])
