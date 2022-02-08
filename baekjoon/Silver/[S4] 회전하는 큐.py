N, M = map(int, input().split())
pop = list(map(int, input().split()))
arr = list(range(1, N + 1))
ans = 0

for x in pop:
    i = arr.index(x)
    ans += min(i, len(arr) - i)
    arr = arr[i + 1:] + arr[:i]

print(ans)
