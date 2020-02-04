input()
p = sorted(list(map(int, input().split())))
ans = 0
for i in range(len(p)): ans += p[i] * (len(p) - i)
print(ans)
