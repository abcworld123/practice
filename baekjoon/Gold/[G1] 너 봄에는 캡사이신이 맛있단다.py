N = int(input())
arr = tuple(sorted(map(int, input().split())))
ans, mod = 0, 1000000007

mods = [1, 2]
for i in range(2, N):
	mods.append(mods[(i >> 1) + (i & 1)] * mods[i >> 1] % mod)

for i in range(N >> 1):
	ans += (mods[N - i - 1] - mods[i]) * (arr[ - i - 1] - arr[i]) % mod

print(ans % mod)
