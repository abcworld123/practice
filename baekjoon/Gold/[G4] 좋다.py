from collections import Counter

input()
arr = list(map(int, input().split()))
counter = Counter(arr)
s = set(arr)
good = set()
length = len(arr)

for i in range(length - 1):
	for j in range(i + 1, length):
		summ = arr[i] + arr[j]
		if summ in s:
			if arr[i] == arr[j] == 0 and counter[0] < 3: continue
			if (arr[i] == 0 and counter[arr[j]] < 2) or (arr[j] == 0 and counter[arr[i]] < 2): continue
			good.add(summ)

print(sum(counter[x] for x in good))
