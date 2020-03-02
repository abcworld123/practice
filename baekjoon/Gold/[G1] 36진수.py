arr, jinsu, _jinsu = {}, {}, [str(c) for c in range(10)] + [chr(c) for c in range(65, 91)]
for i in range(36): jinsu[_jinsu[i]] = i

for i in range(int(input())):
	expr = input().strip()[::-1]
	for j in range(len(expr)):
		if expr[j] not in arr: arr[expr[j]] = 36 ** j
		else: arr[expr[j]] += 36 ** j

K = int(input())
_arr = arr.copy()
for c in list(arr.keys()): _arr[c] = abs(_arr[c] * 35 - _arr[c] * jinsu[c])
desc = sorted(_arr.items(), key=lambda x: -x[1])
for i in range(len(arr)): arr[desc[i][0]] = arr[desc[i][0]] * 35 if i < K else arr[desc[i][0]] * jinsu[desc[i][0]]

ans, result = [], sum(arr.values())
if result:
	while result:
		result, c = divmod(result, 36)
		ans.append(c)
	for n in ans[::-1]: print(n if n < 10 else chr(n + 55), end='')
else: print(0)
