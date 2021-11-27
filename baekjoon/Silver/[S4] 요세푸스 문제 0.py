N, K = map(int, input().split())
arr = list(range(1, N + 1))
ans, cur = [], 0

while arr:
    cur = (cur + K - 1) % len(arr)
    ans.append(arr.pop(cur))

print(f'<{str(ans)[1: -1]}>')
