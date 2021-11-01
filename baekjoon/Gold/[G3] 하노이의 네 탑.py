arr = [0]
for i in range(45):
	for j in range(i + 1):
		arr.append(arr[-1] + (2 ** i))

for i, x in enumerate([*open(0)]):
	print(f'Case {i + 1}: {arr[int(x)]}')


# 도출 과정
arr3 = [0, 1, 3, 5]
arr2 = [0] + [2 ** x - 1 for x in range(1, 1002)]

for i in range(4, 1002):
	arr3.append(min([arr3[a] * 2 + arr2[i - a] for a in range(1, i)]))

print(arr3)
