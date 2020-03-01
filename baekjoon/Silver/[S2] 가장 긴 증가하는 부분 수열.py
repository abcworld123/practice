input()
arr = list(map(int, input().split()))

for i in range(len(arr)):
	arr[i] = [arr[i], 0]
	less = [x for x in arr[:i] if x[0] < arr[i][0]]
	arr[i][1] = max(less, key=lambda x: x[1])[1] + 1 if len(less) else 1

print(max(arr, key=lambda x: x[1])[1])
