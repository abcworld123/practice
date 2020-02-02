x = int(input())
arr = [0, 0, 1, 1]

for x in range(4, x + 1):
    b, c = 99, 99
    a = arr[x - 1]
    if x % 2 == 0: b = arr[x // 2]
    if x % 3 == 0: c = arr[x // 3]
    arr += [min(a, b, c) + 1]

print(arr[x])
