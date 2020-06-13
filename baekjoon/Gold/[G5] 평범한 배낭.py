n, w = map(int, input().split())
arr = [[0] * (w + 1)]
items = [[-1, -1]]
for i in range(n): items.append(list(map(int, input().split())))

for i in range(1, n + 1):
	cur_w, cur_c = items[i][0], items[i][1]
	arr.append([])
	for j in range(w + 1):
		if j < cur_w: arr[-1].append(arr[i - 1][j])
		else:arr[-1].append(max(arr[i - 1][j - cur_w] + cur_c, arr[i - 1][j]))

print(arr[-1][-1])
