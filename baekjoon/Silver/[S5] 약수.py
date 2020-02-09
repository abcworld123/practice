input()
arr = list(map(int, input().split()))
print(min(arr) * max(arr)) if len(arr) > 1 else print(arr[0] ** 2)
