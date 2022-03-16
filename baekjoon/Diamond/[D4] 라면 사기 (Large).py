import sys
input = sys.stdin.buffer.readline

N, B, C = map(int, input().split())
arr = list(map(int, input().split())) + [0, 0]
ans = 0

if B <= C:
    print(B * sum(arr))
    exit()

for i in range(N):
    while arr[i]:
        if arr[i + 1]:
            if arr[i + 2]:
                if arr[i + 1] > arr[i + 2]:
                    x = min(arr[i], arr[i + 1] - arr[i + 2])
                    arr[i] -= x
                    arr[i + 1] -= x
                    ans += (B + C) * x
                else:
                    x = min(arr[i], arr[i + 1], arr[i + 2])
                    arr[i] -= x
                    arr[i + 1] -= x
                    arr[i + 2] -= x
                    ans += (B + 2 * C) * x
            else:
                x = min(arr[i], arr[i + 1])
                arr[i] -= x
                arr[i + 1] -= x
                ans += (B + C) * x
        else:
            ans += B * arr[i]
            arr[i] = 0

print(ans)
