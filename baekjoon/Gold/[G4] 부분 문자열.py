# kmp
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
	while i < len(a):
		if a[i] == b[j]:
			i += 1
			j += 1
			if j == len(b): return 1
		else:
			if j == 0: i -= table[j]
			else: j = table[j]
	return 0

stdin = [*open(0)]
a = stdin[0]
b = stdin[1].replace('\n', '')
table = makeTable(b)
ans = search(table, a, b)
print(ans)



# 숏코딩
import re
a=input()
print(1if re.search(input(),a)else 0)
