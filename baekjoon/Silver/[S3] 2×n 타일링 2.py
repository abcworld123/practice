n = int(input())
a, b = 1, 1
for _ in range(n - 1): a, b = b, 2 * a + b
print(b % 10007)
