def makeTable(s):
	table = [0] * len(s)
	j = 0
	for i in range(1, len(s)):
		while j > 0 and s[i] != s[j]:
			j = table[j - 1]
		if s[i] == s[j]:
			j += 1
			table[i] = j
	return [-1] + table


def search(table, a, b):
	i, j = 0, 0
	arr = []
	while i < len(a):
		if a[i] == b[j]:
			i += 1
			j += 1
			if j == len(b):
				arr.append(i - len(b) + 1)
				j = table[j]
		else:
			if j == 0: i -= table[j]
			else: j = table[j]
	return arr

stdin = [*open(0)]
a = stdin[0]
b = stdin[1].replace('\n', '')
table = makeTable(b)
arr = search(table, a, b)
print(len(arr))
for x in arr: print(x)
