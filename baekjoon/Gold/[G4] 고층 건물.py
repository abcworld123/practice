def f(a, b, c):
    m = -9999999999
    for j in range(a, b, c):
        if t[i][j] > m: m = t[i][j];r[i] += 1

input()
s, t = list(map(int, input().split())), []
n = len(s)
r = [0] * n
for i in range(n):
    t.append([])
    for j in range(n): t[i].append((s[j] - s[i]) / abs(i - j) if i != j else 0)
for i in range(n): f(i - 1, -1, -1);f(i + 1, n, 1)
print(max(r))
