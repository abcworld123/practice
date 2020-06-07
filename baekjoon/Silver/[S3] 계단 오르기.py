n = int(input())
if n == 1: print(input()); exit()
a = []
for i in range(n): a.append(int(input()))
ans = [[a[0], 0], [a[0] + a[1], a[1]]]
for i in range(2, n): ans.append([ans[i - 1][1] + a[i], max(ans[i - 2]) + a[i]])
print(max(ans[n - 1]))
