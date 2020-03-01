n = int(input())
a = list(map(int, input().split()))
c = [0] * 1001
for i in range(n): c[a[i]] = max(c[:a[i]]) + a[i]
print(max(c))
