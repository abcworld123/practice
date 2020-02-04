n = int(input())
p = [1, 1]
for i in range(2, n + 1): p += [p[i - 1] + p[i - 2]]
print(p[n] % 10007)
