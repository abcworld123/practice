arr, exprs, dont_zero = {}, [], set()

for i in range(int(input())):
	exprs.append(input())
	expr = exprs[-1][::-1]
	dont_zero.add(expr[-1])
	for j in range(len(expr)):
		if expr[j] not in arr: arr[expr[j]] = 10 ** j
		else: arr[expr[j]] += 10 ** j

asec = sorted(arr.items(), key=lambda x: x[1])
if len(arr) == 10:
	for i in range(len(arr)):
		if asec[i][0] not in dont_zero: arr[asec[i][0]] = 0; break

num = 9
desc = sorted(arr.items(), key=lambda x: -x[1])
for i in range(len(arr)):
	arr[desc[i][0]] = int(desc[i][1]) * num
	if arr[desc[i][0]]: num -= 1

print(sum(arr.values()))
