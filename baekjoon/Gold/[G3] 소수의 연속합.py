def prime(n):
    if n < 2: return []
    n += 1
    save = [1] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if save[i // 2]: save[i * i // 2::i] = [0] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]

N = int(input())
arr = [0] + prime(N)
for i in range(1, len(arr)): arr[i] += arr[i - 1]
a, b = 0, 1
ans = 0

while a < b < len(arr):
    s = arr[b] - arr[a]
    if s <= N:
        if s == N: ans += 1
        b += 1
    else: a += 1

print(ans)
