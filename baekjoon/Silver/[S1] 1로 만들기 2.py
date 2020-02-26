N = int(input())
arr = [[0, 0], [0, 0], [1, 2], [1, 3]]

for N in range(4, N + 1):
    a = [arr[N - 1][0] + 1, 1]
    b = [arr[N // 2][0] + 1, 2] if N % 2 == 0 else [99, 2]
    c = [arr[N // 3][0] + 1, 3] if N % 3 == 0 else [99, 3]
    arr.append(min(a, b, c, key=lambda x: x[0]))

print(arr[N][0])
print(N, end=' ')
while N != 1:
    if arr[N][1] == 1: N -= 1
    else: N //= arr[N][1]
    print(N, end=' ')
