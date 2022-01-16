N, K = map(int, input().split())
b = K - sum(map(int, input().split()))
ans, mod = 1, 1000000007
for i in range(1, N + 1):
    ans = ans * (b + i) % 1000000007
print(ans)
