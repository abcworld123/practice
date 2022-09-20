def sums(a, d, x, n, i):
    if i >= n:
        d[x] += 1
        return
    sums(a, d, x, n, i + 1)
    sums(a, d, x + a[i], n, i + 1)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
a, b = arr[:N // 2], arr[N // 2:]
sa, sb = [0] * 4000001, [0] * 5000001
ans = 0

sums(a, sa, 0, len(a), 0)
sums(b, sb, 0, len(b), 0)
sa[0] -= 1
sb[0] -= 1

for x in range(-2000000, 2000001):
    ans += sa[x] * sb[S - x]
ans += sa[S] + sb[S]

print(ans)
