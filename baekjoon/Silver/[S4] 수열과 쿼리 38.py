import sys

arr = list(map(int, sys.stdin.buffer.read().split()))
N, i = arr[0], 1
s, x = 0, 0
ans = []

for _ in range(N):
    if arr[i] == 1:
        s += arr[i + 1]
        x ^= arr[i + 1]
        i += 2
    elif arr[i] == 2:
        s -= arr[i + 1]
        x ^= arr[i + 1]
        i += 2
    elif arr[i] == 3:
        ans.append(s)
        i += 1
    else:
        ans.append(x)
        i += 1

print('\n'.join(map(str, ans)))
