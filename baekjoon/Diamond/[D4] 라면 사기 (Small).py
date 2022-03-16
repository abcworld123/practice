import sys
input = sys.stdin.buffer.readline

N = int(input())
arr = list(map(int, input().split())) + [0, 0]
ans = 0

for i in range(N):
    while arr[i]:
        if arr[i + 1]:
            if arr[i + 2]:
                if arr[i + 1] > arr[i + 2]:
                    x = min(arr[i], arr[i + 1] - arr[i + 2])
                    arr[i] -= x
                    arr[i + 1] -= x
                    ans += 5 * x
                else:
                    x = min(arr[i], arr[i + 1], arr[i + 2])
                    arr[i] -= x
                    arr[i + 1] -= x
                    arr[i + 2] -= x
                    ans += 7 * x
            else:
                x = min(arr[i], arr[i + 1])
                arr[i] -= x
                arr[i + 1] -= x
                ans += 5 * x
        else:
            ans += 3 * arr[i]
            arr[i] = 0

print(ans)
